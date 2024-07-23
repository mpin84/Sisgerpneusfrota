import tkinter as tk
from tkinter import messagebox


class FleetManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão de Frota")

        self.fleet = []

        self.create_widgets()

    def create_widgets(self):
        # Frame para adicionar veículos
        self.add_frame = tk.Frame(self.root)
        self.add_frame.pack(pady=10)

        tk.Label(self.add_frame, text="Marca:").grid(row=0, column=0, padx=5)
        self.brand_entry = tk.Entry(self.add_frame)
        self.brand_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.add_frame, text="Modelo:").grid(row=1, column=0, padx=5)
        self.model_entry = tk.Entry(self.add_frame)
        self.model_entry.grid(row=1, column=1, padx=5)

        tk.Label(self.add_frame, text="Chassi:").grid(row=2, column=0, padx=5)
        self.chassis_entry = tk.Entry(self.add_frame)
        self.chassis_entry.grid(row=2, column=1, padx=5)

        tk.Label(self.add_frame, text="Placa:").grid(row=3, column=0, padx=5)
        self.plate_entry = tk.Entry(self.add_frame)
        self.plate_entry.grid(row=3, column=1, padx=5)

        tk.Label(self.add_frame, text="Renavam:").grid(row=4, column=0, padx=5)
        self.renavam_entry = tk.Entry(self.add_frame)
        self.renavam_entry.grid(row=4, column=1, padx=5)

        tk.Label(self.add_frame, text="Combustível:").grid(row=5, column=0, padx=5)
        self.fuel_entry = tk.Entry(self.add_frame)
        self.fuel_entry.grid(row=5, column=1, padx=5)

        tk.Label(self.add_frame, text="Qtd pneus:").grid(row=6, column=0, padx=5)
        self.tyreqtd_entry = tk.Entry(self.add_frame)
        self.tyreqtd_entry.grid(row=6, column=1, padx=5)

        tk.Button(self.add_frame, text="Adicionar Veículo", command=self.add_vehicle).grid(row=8, column=0,
                                                                                           columnspan=2, pady=10)

        # Frame para exibir a frota
        self.view_frame = tk.Frame(self.root)
        self.view_frame.pack(pady=10)

        self.fleet_listbox = tk.Listbox(self.view_frame, width=50, height=10)
        self.fleet_listbox.pack(side=tk.LEFT, padx=10)

        self.scrollbar = tk.Scrollbar(self.view_frame, orient=tk.VERTICAL, command=self.fleet_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.fleet_listbox.config(yscrollcommand=self.scrollbar.set)

        # Botão para remover veículo
        tk.Button(self.root, text="Remover Veículo", command=self.remove_vehicle).pack(pady=10)

    def add_vehicle(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        chassis = self.model_entry.get()
        plate = self.plate_entry.get()
        renavam = self.renavam_entry.get()
        fuel = self.fuel_entry.get()
        tyreqtd = self.tyreqtd_entry.get()

        if model and plate:
            vehicle = f"{model} - {plate}"
            self.fleet.append(vehicle)
            self.update_fleet_listbox()
            self.model_entry.delete(0, tk.END)
            self.plate_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos")

    def update_fleet_listbox(self):
        self.fleet_listbox.delete(0, tk.END)
        for vehicle in self.fleet:
            self.fleet_listbox.insert(tk.END, vehicle)

    def remove_vehicle(self):
        selected_index = self.fleet_listbox.curselection()
        if selected_index:
            del self.fleet[selected_index[0]]
            self.update_fleet_listbox()
        else:
            messagebox.showwarning("Seleção inválida", "Por favor, selecione um veículo para remover")


if __name__ == "__main__":
    root = tk.Tk()
    app = FleetManagementSystem(root)
    root.mainloop()