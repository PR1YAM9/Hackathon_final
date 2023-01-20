# Dictionary to map symptoms to diseases

# Function to get the disease based on symptoms
def get_disease(symptoms):
    disease_symptoms = {
        "malaria": {
            "symptoms":["abdomen pain", "muscle", "chills", "fever","sweating", "fatigue","diarrhoea"],
            "description":"A disease caused by a plasmodium parasite, transmitted by the bite of infected mosquitoes.The severity of malaria varies based on the species of plasmodium.There are 5 parasite species that cause malaria in humans, and 2 of these species – P. falciparum and P. vivax – pose the greatest threat.",
            "treatments":"People travelling to areas where malaria is common typically take protective drugs before, during and after their trip. Treatment includes antimalarial drugs.",
        },
        
        "leptospirosis":{
            "symptoms":["muscle pain", "headache", "high" "fever", "chills", "red eyes", "vomiting", "skin rash", "sore throat"],
            "description":"Muscle Pain,Headache,High Fever, Chills,Red Eyes,Vomiting,Skin Rash,Sore Throat",
            "treatment":"Treatment consists of antibiotics which clear the infection"
        },
        
        "hepattits-b":{
            "symptoms":["abdominal pain", "dark urine", "yellow eyes", "yellow skin", "joint pain", "loss in appetite", "nausea"],
            "description":"A serious liver infection caused by the hepatitis B virus that's easily preventable by a vaccine.This disease is most commonly spread by exposure to infected bodily fluids.",
            "treatment":":Treatment depends on severity.The condition often clears up on its own. Chronic cases require medication and possibly a liver transplant."
        },
        
        "flu":{
            "symptoms":["fever", "chills", "cough", "congestion", "muscle pain", "runny nose", "fatigue", "headachde"],
            "description":"A common viral infection that can be deadly, especially in high-risk groups.The flu attacks the lungs, nose and throat. Young children, older adults, pregnant women and people with chronic disease or weak immune systems are at high risk.",
            "treatments":"Flu is primarily treated with rest and fluid intake to allow the body to fight the infection on its own. Paracetamol may help cure the symptoms but NSAIDs should be avoided. An annual vaccine can help prevent the flu and limit its complications."
        },
        
        "typhoid":{
            "symptoms":["headache", "muscle weakness", "fever", "fatigue", "chills", "rash with red dots", "weight loss"],
            "description":"Typhoid fever is an infection that spreads through contaminated food and water.",
            "treatments":"Treatment includes antibiotics and fluids."
        },
        "dengue":{
            "symptoms":["high fever", "headache", "rash", "muscle pain", "joint pain", "back pain"],
            "description":"",
            "treatments":"",
        },
        
        "amoebiasis":{
            "symptoms":["diarrhea", "weight loss", "blood in stool", "loss of appetite", "gas"],
            "description" :"A parasitic infection of the colon with the amoeba Entamoeba histolytica.Amoebiasis infection is most common in tropical areas with untreated water. It spreads through drinking or eating uncooked food, such as fruit, that may have been washed in contaminated local water.",
            "treatments":"Treatment includes fluids and pain relievers. Severe cases require hospital care.",
        },
        
        "cholera":{
            "symptoms":["dehydration", "nausea", "vomiting", "abdomin pain", "watery diarrhea", "lethargic"],
            "description" :"",
            "treatments":"",
        },
        
        "tuberculosis":{
            "symptoms":["blood in cough, weight loss, loss of appetite, night sweats, pain in chest, phelgm, "],
            "description" :"A potentially serious infectious bacterial disease that mainly affects the lungs.The bacteria that cause TB are spread when an infected person coughs or sneezes.Most people infected with the bacteria that cause tuberculosis don't have symptoms",
            "treatments":"Treatment isn't always required for those without symptoms. Patients with active symptoms will require a long course of treatment involving multiple antibiotics.",
        },
        
        "brucellosis":{
            "symptoms":["blood in cough", "weight loss", "loss of appetite", "night sweats", "pain in chest", "phelgm"],
            "description" :"An infection spread from animals to people, mostly by unpasteurised dairy products.Brucellosis is a bacterial infection that affects thousands of people worldwide. Avoiding unpasteurised dairy products and taking precautions when working with animals or in a laboratory can help prevent brucellosis.",
            "treatments":"Treatment includes antibiotics. Relapses are common.",
        },
        "pneumoconiosis":{
            "symptoms":['cough','shortness of breadth', "chest tightness", "mucus"],
            "description" :"The pneumoconioses are a group of lung diseases caused by the lung's reaction inhaling certain dusts. The main cause of the pneumoconioses is work-place exposure. Environmental exposures have rarely been related to these diseases. The primary pneumoconioses are: Abestosis – caused by inhaling asbestos fibers.",
            "treatments":"Pneumoconiosis can't be cured. Once the disease has been diagnosed, treatment is aimed at keeping it from getting worse and controlling your symptoms.",
        },
        "ringworm":{
            "symptoms":["ring shaped rash","itchy", "dry skin"],
            "description" :"A highly contagious fungal infection of the skin or scalp.Ringworm is spread by skin-to-skin contact or by touching an infected animal or object.Ringworm is typically scaly and may be red and itchy. Ringworm of the scalp is common in children, where it may cause bald patches.",
            "treatments":"The treatment for ringworm is antifungal medication.",
        },
            
        "monkeypox":{
            "symptoms":["fever","headache","body aches","swollen lymph","rash"],
            "description" :"Monkeypox is caused by monkeypox virus, a member of the Orthopoxvirus genus in the family Poxviridae.Monkeypox is usually a self-limited disease with the symptoms lasting from 2 to 4 weeks. Severe cases can occur. In recent times, the case fatality ratio has been around 3–6%.Monkeypox is transmitted to humans through close contact with an infected person or animal, or with material contaminated with the virus.",
            "treatments":"Currently, there is no specific treatment approved for mpox. However, there are several antiviral medications used to treat smallpox and other conditions that may help patients with mpox.",
        },
        "Measles":{
            "symptoms":["fever", "cough", "runny nose", "watery eyes", "red eyes"],
            "description" :"A viral infection that's serious for small children but is easily preventable by a vaccine.The disease spreads through the air by respiratory droplets produced from coughing or sneezing.Measles symptoms don't appear until 10 to 14 days after exposure.",
            "treatments":"There's no treatment to get rid of an established measles infection, but over-the-counter fever reducers or vitamin A may help with symptoms.",
        },
        "Hantavirus":{
            "symptoms":["fatigue", "fever" ,"muscle pain" , "headaches", "dizziness", "chills","nausea", "vomiting","diarrhoea", "abdominal pain"],
            "description" :"Hantaviruses are a family of viruses spread mainly by rodents and can cause varied disease syndromes in people worldwide.  Infection with any hantavirus can produce hantavirus disease in people.",
            "treatments":"There is no specific treatment, cure, or vaccine for hantavirus infection. However, we do know that if infected individuals are recognized early and receive medical care in an intensive care unit, they may do better.",
        },
        "hookworm infection":{
            "symptoms":["itchy", "rash in foot", "abdominal pain", "diarrhoea", "loss of appetite", "weight loss", "fatigue", "anaemia"],
            "description" :"Hookworms live in the small intestine. Hookworm eggs are passed in the feces of an infected person.The larvae mature into a form that can penetrate the skin of humans. Hookworm infection is mainly acquired by walking barefoot on contaminated soil. One kind of hookworm can also be transmitted through the ingestion of larvae.",
            "treatments":"Anthelminthic medications, such as albendazole and mebendazole, are the drugs of choice for treatment of hookworm infections. Infections are generally treated for 1-3 days. The recommended medications are effective and appear to have few side effects.",
        },
        "filariasis":{
            "symptoms":["swollen legs","swollen arms","swollen genitalia"],
            "description" :"Lymphatic filariasis, considered globally as a neglected tropical disease (NTD), is a parasitic disease caused by microscopic, thread-like worms. The adult worms only live in the human lymph system. The lymph system maintains the body's fluid balance and fights infections.",
            "treatments":"The main goal of treatment of an infected person is to kill the adult worm. Diethylcarbamazine citrate (DEC), which is both microfilaricidal and active against the adult worm, is the drug of choice for lymphatic filariasis. The late phase of chronic disease is not affected by chemotherapy.",
        },
        "chicken pox":{
            "symptoms":["rash", "itchy", "blisters"],
            "description" :"A highly contagious viral infection which is  is highly contagious to those who haven't had the disease or been vaccinated against it",
            "treatments":":Chickenpox can be prevented by a vaccine. Treatment usually involves relieving symptoms, although high-risk groups may receive antiviral medication. ",
        },
        "common cold":{
            "symptoms":["Cough", "phlegm", "congestion", "runny nose", "sneezing", "loss of smell", "redness", "post-nasal drip", "watery eyes", "chest pressure", "headache", "swollen lymph","throat irritation"],
            "description" :"A common viral infection of the nose and throat.In contrast to the flu, a common cold can be caused by many different types of viruses. The condition is generally harmless and symptoms usually resolve within two weeks.",
            "treatments":"",
        },
        "conjunctivitis":{
            "symptoms":["red eye","puffy eye", "watery eye","runny nose", "sneezing"],
            "description" :"Inflammation or infection of the outer membrane of the eyeball and the inner eyelid.Conjunctivitis, or pink eye, is an irritation or inflammation of the conjunctiva, which covers the white part of the eyeball. It can be caused by allergies or a bacterial or viral infection. Conjunctivitis can be extremely contagious and is spread by contact with eye secretions from someone who is infected",
            "treatments":"",
        },
        "Meningitis":{
            "symptoms":["muscle pain", "fever", "chills", "fatigue", "lethargy", "loss of appetite", "malaise", "shivering", "fast breathing", "sleepiness"],
            "description" :"Inflammation of brain and spinal cord membranes, typically caused by an infection.Meningitis is usually caused by a viral infection but can also be bacterial or fungal. Vaccines can prevent some forms of meningitis.",
            "treatments":"Depending on the cause, meningitis may get better on its own or it can be life-threatening, requiring urgent antibiotic treatment.",
        },
        "mumps":{
            "symptoms":["dry mouth", "headache", "hearing loss", "neck swelling", "swollen lymph nodes","swollen salivary glands"],
            "description" :"A viral infection that affects the salivary glands that's easily preventable by a vaccine.Mumps affects the parotid glands, salivary glands below and in front of the ears. The disease spreads through infected saliva.",
            "treatments":":Treatment focuses on symptom relief. Recovery takes about two weeks. The disease can be prevented by the MMR vaccine",
        },
    }
    disease_probability = {}
    for disease, symptom_info in disease_symptoms.items():
        symptom_list = symptom_info["symptoms"]
        common_symptoms = set(symptoms) & set(symptom_list)
        disease_probability[disease] = len(common_symptoms) / len(symptom_list)
    top_diseases = sorted(disease_probability.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        disease = top_diseases[i][0]
        description = disease_symptoms[disease]["description"]
        treatments = disease_symptoms[disease]["treatments"]
        return (f"Disease: {disease}\nDescription: {description}\nTreatments: {treatments}\n")
