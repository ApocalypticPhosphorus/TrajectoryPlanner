import tkinter

def launch():
    print("launching")
    
    launch_site_params = {
        "latitude":latitude_entry.get(),
        "longitude":longitude_entry.get(),
        "elevation":elevation_entry.get()
    }
    
    rocket_params = {
        "fsm":first_stage_mass_entry.get(),
        "fsf":first_stage_fuel_mass_entry.get(),
        "fst":first_stage_thrust_entry.get(),
        "fsb":first_stage_burn_time_entry.get(),
        "ssm":second_stage_mass_entry.get(),
        "ssf":second_stage_fuel_mass_entry.get(),
        "sst":second_stage_thrust_entry.get(),
        "ssb":second_stage_burn_time_entry.get(),
        "faring mass":fairing_mass_entry.get(),
        "payload mass":payload_mass_entry.get(),
        "drag":drag_entry.get(),
    }
    
    orbit_params = {
        "eccentricity":eccentricity_entry.get(),
        "semimajor axis":semimajor_axis_entry.get(),
        "inclination":inclination_entry.get(),
        "ascending node":longitude_ascending_node_entry.get(),
        "argument of perapsis":argument_of_perapsis_entry.get()
    }
    
    print(launch_site_params)
    print(rocket_params)
    print(orbit_params)

window = tkinter.Tk()
window.title("Launch Parameters")

frame = tkinter.Frame(window)
frame.pack()

launch_site_frame = tkinter.LabelFrame(frame,text="Launch Site")
launch_site_frame.grid(row=0,column=0, sticky="n")

latitude_label = tkinter.Label(launch_site_frame,text="Latitude")
latitude_label.grid(row=0,column=0)
latitude_entry = tkinter.Entry(launch_site_frame)
latitude_entry.grid(row=1,column=0)

longitude_label = tkinter.Label(launch_site_frame,text="Longitude")
longitude_label.grid(row=2,column=0)
longitude_entry = tkinter.Entry(launch_site_frame)
longitude_entry.grid(row=3,column=0)

elevation_label = tkinter.Label(launch_site_frame,text="Elevation")
elevation_label.grid(row=4,column=0)
elevation_entry = tkinter.Entry(launch_site_frame)
elevation_entry.grid(row=5,column=0)

for widget in launch_site_frame.winfo_children():
    widget.grid_configure(pady=1, padx=1)
    
rocket_frame = tkinter.LabelFrame(frame,text="Rocket")
rocket_frame.grid(row=0,column=1)

first_stage_mass_label = tkinter.Label(rocket_frame,text="First Stage Mass")
first_stage_mass_label.grid(row=0,column=0)
first_stage_mass_entry = tkinter.Entry(rocket_frame)
first_stage_mass_entry.grid(row=1,column=0)

first_stage_fuel_mass_label = tkinter.Label(rocket_frame,text="First Stage Fuel Mass")
first_stage_fuel_mass_label.grid(row=2,column=0)
first_stage_fuel_mass_entry = tkinter.Entry(rocket_frame)
first_stage_fuel_mass_entry.grid(row=3,column=0)

first_stage_thrust_label = tkinter.Label(rocket_frame,text="First Stage Thrust")
first_stage_thrust_label.grid(row=4,column=0)
first_stage_thrust_entry = tkinter.Entry(rocket_frame)
first_stage_thrust_entry.grid(row=5,column=0)

first_stage_burn_time_label = tkinter.Label(rocket_frame,text="First Stage Burn Time")
first_stage_burn_time_label.grid(row=6,column=0)
first_stage_burn_time_entry = tkinter.Entry(rocket_frame)
first_stage_burn_time_entry.grid(row=7,column=0)

second_stage_mass_label = tkinter.Label(rocket_frame,text="Second Stage Mass")
second_stage_mass_label.grid(row=8,column=0)
second_stage_mass_entry = tkinter.Entry(rocket_frame)
second_stage_mass_entry.grid(row=9,column=0)

second_stage_fuel_mass_label = tkinter.Label(rocket_frame,text="Second Stage Fuel Mass")
second_stage_fuel_mass_label.grid(row=10,column=0)
second_stage_fuel_mass_entry = tkinter.Entry(rocket_frame)
second_stage_fuel_mass_entry.grid(row=11,column=0)

second_stage_thrust_label = tkinter.Label(rocket_frame,text="Second Stage Thrust")
second_stage_thrust_label.grid(row=12,column=0)
second_stage_thrust_entry = tkinter.Entry(rocket_frame)
second_stage_thrust_entry.grid(row=13,column=0)

second_stage_burn_time_label = tkinter.Label(rocket_frame,text="Second Stage Burn Time")
second_stage_burn_time_label.grid(row=14,column=0)
second_stage_burn_time_entry = tkinter.Entry(rocket_frame)
second_stage_burn_time_entry.grid(row=15,column=0)

fairing_mass_label = tkinter.Label(rocket_frame,text="Fairing Mass")
fairing_mass_label.grid(row=16,column=0)
fairing_mass_entry = tkinter.Entry(rocket_frame)
fairing_mass_entry.grid(row=17,column=0)

payload_mass_label = tkinter.Label(rocket_frame,text="Payload Mass")
payload_mass_label.grid(row=18,column=0)
payload_mass_entry = tkinter.Entry(rocket_frame)
payload_mass_entry.grid(row=19,column=0)

drag_label = tkinter.Label(rocket_frame,text="Drag")
drag_label.grid(row=20,column=0)
drag_entry = tkinter.Entry(rocket_frame)
drag_entry.grid(row=21,column=0)

for widget in rocket_frame.winfo_children():
    widget.grid_configure(pady=1, padx=1)
    
orbit_frame = tkinter.LabelFrame(frame,text="Orbit")
orbit_frame.grid(row=0,column=2, sticky="n")

eccentricity_label = tkinter.Label(orbit_frame,text="Eccentricity")
eccentricity_label.grid(row=0,column=0)
eccentricity_entry = tkinter.Entry(orbit_frame)
eccentricity_entry.grid(row=1,column=0)

semimajor_axis_label = tkinter.Label(orbit_frame,text="Semimajor Axis")
semimajor_axis_label.grid(row=2,column=0)
semimajor_axis_entry = tkinter.Entry(orbit_frame)
semimajor_axis_entry.grid(row=3,column=0)

inclination_label = tkinter.Label(orbit_frame,text="Inclination")
inclination_label.grid(row=4,column=0)
inclination_entry = tkinter.Entry(orbit_frame)
inclination_entry.grid(row=5,column=0)

longitude_ascending_node_label = tkinter.Label(orbit_frame,text="Ascending Node")
longitude_ascending_node_label.grid(row=6,column=0)
longitude_ascending_node_entry = tkinter.Entry(orbit_frame)
longitude_ascending_node_entry.grid(row=7,column=0)

argument_of_perapsis_label = tkinter.Label(orbit_frame,text="Argument of Perapsis")
argument_of_perapsis_label.grid(row=8,column=0)
argument_of_perapsis_entry = tkinter.Entry(orbit_frame)
argument_of_perapsis_entry.grid(row=9,column=0)

for widget in orbit_frame.winfo_children():
    widget.grid_configure(pady=1, padx=1)

launch_button = tkinter.Button(frame, text="Launch!", command=launch)
launch_button.grid(row=0,column=0)



window.mainloop()