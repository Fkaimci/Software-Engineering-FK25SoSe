from my_functions import build_experiment
from my_functions import build_person
from my_functions import estimate_max_hr

if __name__ == "__main__":
    experiment = build_experiment(
        experiment_name="Leistungstest1",
        date="19.03.25",
        supervisor="Franka",
        subject="Leistungstest"
    )

    patient = build_person(
        first_name="Marius",
        last_name="Valenta",
        sex="male",
        age=19.0
    )
    
    herzfrequenz = estimate_max_hr(
        age_years=19.0,
        sex = "male"

    )
    #print(patient)
    #print(experiment)







    def dict_komplett(patient, experiment) -> dict:

       dict_ganz = { "Patient:innen_Daten" : patient,
                "Experiment_Daten" : experiment,
                }
       return dict_ganz
    
    print(dict_komplett(patient,experiment))
