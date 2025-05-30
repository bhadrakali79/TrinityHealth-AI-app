import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# =============== Page Config ===============
st.set_page_config(page_title="TrinityHealth AI - Multi Disease Prediction",
                   layout="wide",
                   initial_sidebar_state="expanded")

# =============== Load Models and Scalers ===============
# Diabetes
diabetes_data = pickle.load(open('C:/Users/DELL/Documents/Project_MSc - Copy/diabetes_model_final2.sav', 'rb'))
diabetes_model = diabetes_data['model']
diabetes_scaler = diabetes_data['scaler']

# Heart Disease
heart_disease_data = pickle.load(open('C:/Users/DELL/Documents/Project_MSc - Copy/heart_disease_model_final.sav', 'rb'))
if isinstance(heart_disease_data, dict):
    heart_disease_model = heart_disease_data['model']
    heart_disease_scaler = heart_disease_data.get('scaler', None)
else:
    heart_disease_model = heart_disease_data
    heart_disease_scaler = None

# Parkinson's
parkinsons_data = pickle.load(open('C:/Users/DELL/Documents/Project_MSc - Copy/parkinsons_model_final2.sav', 'rb'))
parkinsons_model = parkinsons_data['model']
parkinsons_scaler = parkinsons_data['scaler']

# =============== Sidebar Menu ===============
with st.sidebar:
    selected = option_menu(
        'TrinityHealth AI - Multi Disease Prediction',
        ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
        icons=['activity', 'heart', 'person'],
        menu_icon='hospital-fill',
        default_index=0
    )

# =============== Diabetes Prediction ===============
if selected == 'Diabetes Prediction':
    st.title('🩸 Diabetes Prediction')
    st.info("""
        **Input Description:**

        1. Number of Pregnancies - Times a woman has been pregnant, which can influence diabetes risk. 

        2. Glucose Level - Blood sugar level; high values often indicate potential diabetes.

        3. Blood Pressure value - Measures force of blood flow; often elevated in diabetic individuals.

        4. Skin Thickness value - Indicates body fat; correlated with insulin resistance and obesity.

        5. Insulin Level - Hormone controlling blood sugar; low or high suggests metabolic issues.

        6. BMI value - Body Mass Index; higher values signal obesity, a diabetes risk factor.

        7. Diabetes Pedigree Function value - Genetic likelihood based on family history of diabetes.

        8. Age of the Person - Risk increases with age, especially over 45 years old.
    """)

    col1, col2, col3 = st.columns(3)
    with col1: Pregnancies = st.text_input('Number of Pregnancies')
    with col2: Glucose = st.text_input('Glucose Level')
    with col3: BloodPressure = st.text_input('Blood Pressure')
    with col1: SkinThickness = st.text_input('Skin Thickness')
    with col2: Insulin = st.text_input('Insulin Level')
    with col3: BMI = st.text_input('BMI')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2: Age = st.text_input('Age')

    if st.button('🔍 Get Diabetes Result'):
        if all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            try:
                input_data = [[float(Pregnancies), float(Glucose), float(BloodPressure),
                               float(SkinThickness), float(Insulin), float(BMI),
                               float(DiabetesPedigreeFunction), float(Age)]]
                scaled_input = diabetes_scaler.transform(input_data)
                prediction = diabetes_model.predict(scaled_input)[0]
                if prediction == 1:
                    st.error('⚠️ The person is diabetic')
                else:
                    st.success('✅ The person is not diabetic')
                    st.balloons()
                    st.info("🌟 Keep up the great work! Maintaining a healthy lifestyle is a wonderful achievement. Keep eating well, staying active, and being awesome!")
            except Exception as e:
                st.warning(f'⚠️ Please enter valid numerical values. Error: {e}')
        else:
            st.warning('⚠️ Please fill all input fields.')

# =============== Heart Disease Prediction ===============
elif selected == 'Heart Disease Prediction':
    st.title('❤️ Heart Disease Prediction')
    st.info("""
        **Input Description:**

        1. Age - Heart disease risk rises with advancing age.

        2. Sex - Gender influences heart disease likelihood; males often have higher risk.

        3. Chest Pain types - Indicates different heart-related discomforts; helps identify cardiac issues.

        4. Resting Blood Pressure - High values stress the heart and arteries.

        5. Serum Cholestoral in mg/dl - High cholesterol clogs arteries, increasing heart disease risk.

        6. Fasting Blood Sugar > 120mg/dl - Elevated levels can damage blood vessels and heart.

        7. Resting ECG results - Electrical activity reveals heart rhythm abnormalities.

        8. Maximum Heart Rate achieved - Reflects cardiac response to physical exertion.

        9. Exercise Induced Angina - Chest pain during exercise signals restricted blood flow.

        10. ST depression induced by exercise - Drop indicates inadequate blood supply to the heart during stress.

        11. Slope of the peak exercise ST segment - Changes suggest abnormalities in heart muscle response.

        12. Major vessels colored by flourosopy - Number of blood vessels affected seen via fluoroscopy.

        13. Thalassemia Type: Thal (0 = normal; 1 = fixed defect; 2 = reversable defect) - Blood disorder impacting oxygen flow and heart health.


    """)

    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input('Age')
    with col2: sex = st.text_input('Sex (0 = Female, 1 = Male)')
    with col3: cp = st.text_input('Chest Pain Type (0-3)')
    with col1: trestbps = st.text_input('Resting Blood Pressure')
    with col2: chol = st.text_input('Cholesterol')
    with col3: fbs = st.text_input('Fasting Blood Sugar')
    with col1: restecg = st.text_input('Resting ECG')
    with col2: thalach = st.text_input('Max Heart Rate')
    with col3: exang = st.text_input('Exercise Induced Angina')
    with col1: oldpeak = st.text_input('Oldpeak')
    with col2: slope = st.text_input('Slope')
    with col3: ca = st.text_input('CA')
    with col1: thal = st.text_input('Thal')

    if st.button('🔍 Get Heart Disease Result'):
        try:
            input_data = [[float(age), float(sex), float(cp), float(trestbps), float(chol),
                          float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak),
                          float(slope), float(ca), float(thal)]]
            if heart_disease_scaler:
                scaled_input = heart_disease_scaler.transform(input_data)
            else:
                scaled_input = input_data
            prediction = heart_disease_model.predict(scaled_input)[0]
            if prediction == 1:
                st.error('⚠️ The person has heart disease')
            else:
                st.success('✅ The person does not have heart disease')
                st.balloons()
                st.info("💖 Fantastic! Your heart is in great shape. Keep nurturing it with balanced meals, regular movement, and plenty of joy!")
        except Exception as e:
            st.warning(f'⚠️ Please enter valid numerical values. Error: {e}')

# =============== Parkinson's Disease Prediction ===============
elif selected == "Parkinson's Prediction":
    st.title("🧠 Parkinson's Disease Prediction")
    st.info("""
        **Input Description:** 
	
	1. MDVP:Fo(Hz) – Average voice pitch; abnormal patterns indicate vocal impairment.
	
	2. MDVP:RAP – Voice frequency variation; measures vocal tremors.
	
	3. Shimmer:APQ3 – Amplitude variability in short speech frames.
	
	4. HNR – Harmonic-to-noise ratio; lower in Parkinson’s due to vocal noise.
	
	5. D2 – Signal complexity; helps detect neurodegenerative patterns.
	
	6. MDVP:Fhi(Hz) – Maximum pitch; reduced control may indicate vocal issues.
	
	7. MDVP:PPQ – Pitch variation over time; another jitter measure.
	
	8. Shimmer:APQ5 – Amplitude variation in longer speech frames.
	
	9. RPDE – Measures irregularity in vocal dynamics.
	
	10. PPE – Pitch deviation measure; increases in Parkinson’s.
	
	11. MDVP:Flo(Hz) – Minimum vocal frequency; reduced in affected individuals.
	
	12. Jitter:DDP – Combined jitter measure indicating frequency disturbance.
	
	13. MDVP:APQ – Measures average variation in amplitude.
	
	14. DFA – Fractal scaling property showing signal randomness.
	
	15. MDVP:Jitter(%) – Frequency perturbation indicating vocal stability.
	
	16. MDVP:Shimmer – Amplitude perturbation showing voice amplitude variation.
	
	17. Shimmer:DDA – Variation of three consecutive shimmer values.
	
	18. Spread1 – Nonlinear dysphonia indicator related to voice modulation.
	
	19. MDVP:Jitter(Abs) – Absolute jitter value in voice frequency.
	
	20. MDVP:Shimmer(dB) – Shimmer in decibels; louder voice fluctuations.
	
	21. NHR – Noise to harmonic ratio; increased noise indicates voice issues.
	
	22. Spread2 – Secondary dysphonia-related voice feature.
    """)

    features = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
                'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
                'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
                'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA',
                'spread1', 'spread2', 'D2', 'PPE']
    cols = st.columns(5)
    values = []

    for i, feature in enumerate(features):
        with cols[i % 5]:
            val = st.text_input(feature)
            values.append(val)

    if st.button("🔍 Get Parkinson's Result"):
        try:
            input_data = [[float(v) for v in values]]
            scaled_input = parkinsons_scaler.transform(input_data)
            prediction = parkinsons_model.predict(scaled_input)[0]
            if prediction == 1:
                st.error("⚠️ The person has Parkinson's disease")
            else:
                st.success("✅ The person does not have Parkinson's disease")
                st.balloons()
                st.info("🧠 Brilliant! Your results look great. Keep your mind and body active, stay positive, and enjoy life to the fullest!")
        except Exception as e:
            st.warning(f'⚠️ Please enter valid numerical values. Error: {e}')
