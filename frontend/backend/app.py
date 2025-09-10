# FarmAI Helper - Disease Database and Diagnosis System
# ============================================
# CROP DISEASE DATABASE
# ============================================

crop_diseases = {
    "rice": {
        "rice_blast": {
            "name": "Rice Blast",
            "symptoms": [
                "brown spots on leaves", 
                "white centers in spots", 
                "wilting of plants", 
                "stunted growth",
                "neck breaking"
            ],
            "weather_conditions": ["high humidity", "cool nights", "wet conditions"],
            "severity": "high",
            "treatment": [
                "Apply Tricyclazole fungicide spray",
                "Remove and burn affected plants",
                "Improve field drainage",
                "Reduce nitrogen fertilizer"
            ],
            "prevention": [
                "Use resistant rice varieties",
                "Proper plant spacing",
                "Avoid over-fertilization",
                "Clean field after harvest"
            ],
            "cost": "₹500-800 per acre treatment"
        },
        
        "bacterial_blight": {
            "name": "Bacterial Leaf Blight",
            "symptoms": [
                "water-soaked lesions",
                "yellow leaf margins",
                "leaves turning brown",
                "wilting from leaf tips",
                "stunted plant growth"
            ],
            "weather_conditions": ["high temperature", "high humidity", "heavy rain"],
            "severity": "medium",
            "treatment": [
                "Spray copper-based fungicide",
                "Remove affected leaves",
                "Apply balanced fertilizer",
                "Improve field sanitation"
            ],
            "prevention": [
                "Use certified seeds",
                "Avoid water logging",
                "Crop rotation with non-rice crops",
                "Clean irrigation channels"
            ],
            "cost": "₹300-500 per acre treatment"
        },
        
        "brown_spot": {
            "name": "Brown Spot Disease",
            "symptoms": [
                "small brown spots on leaves",
                "dark brown lesions",
                "premature leaf drying",
                "reduced grain filling",
                "poor grain quality"
            ],
            "weather_conditions": ["nutrient deficiency", "drought stress", "poor soil"],
            "severity": "medium",
            "treatment": [
                "Apply potassium fertilizer",
                "Spray Mancozeb fungicide",
                "Improve soil nutrition",
                "Ensure proper irrigation"
            ],
            "prevention": [
                "Balanced fertilization",
                "Use healthy seeds",
                "Maintain soil fertility",
                "Avoid water stress"
            ],
            "cost": "₹400-600 per acre treatment"
        }
    },
    
    "wheat": {
        "rust_disease": {
            "name": "Wheat Rust",
            "symptoms": [
                "reddish-brown spots on leaves",
                "yellow powder on leaves",
                "premature leaf death",
                "reduced grain weight",
                "weak stems"
            ],
            "weather_conditions": ["moderate temperature", "high humidity", "dew formation"],
            "severity": "high",
            "treatment": [
                "Apply Propiconazole spray",
                "Use systemic fungicides",
                "Remove infected plant debris",
                "Apply zinc sulfate"
            ],
            "prevention": [
                "Plant rust-resistant varieties",
                "Avoid late sowing",
                "Proper field sanitation",
                "Balanced nutrition"
            ],
            "cost": "₹600-900 per acre treatment"
        },
        
        "powdery_mildew": {
            "name": "Powdery Mildew",
            "symptoms": [
                "white powdery patches",
                "leaves turning yellow",
                "stunted plant growth",
                "reduced tillering",
                "poor grain development"
            ],
            "weather_conditions": ["cool weather", "high humidity", "cloudy days"],
            "severity": "medium",
            "treatment": [
                "Spray sulfur-based fungicide",
                "Apply Triadimefon",
                "Improve air circulation",
                "Remove affected leaves"
            ],
            "prevention": [
                "Use resistant varieties",
                "Avoid dense planting",
                "Proper field ventilation",
                "Timely sowing"
            ],
            "cost": "₹400-700 per acre treatment"
        }
    },
    
    "tomato": {
        "early_blight": {
            "name": "Early Blight",
            "symptoms": [
                "dark spots with rings",
                "yellowing of lower leaves",
                "leaf drop",
                "stem lesions",
                "fruit rot"
            ],
            "weather_conditions": ["warm temperature", "high humidity", "wet leaves"],
            "severity": "high",
            "treatment": [
                "Apply Chlorothalonil spray",
                "Remove affected leaves",
                "Improve air circulation",
                "Avoid overhead watering"
            ],
            "prevention": [
                "Use disease-free seeds",
                "Crop rotation",
                "Proper plant spacing",
                "Drip irrigation"
            ],
            "cost": "₹800-1200 per acre treatment"
        },
        
        "late_blight": {
            "name": "Late Blight",
            "symptoms": [
                "water-soaked dark spots",
                "white mold on leaf undersides",
                "rapid plant collapse",
                "fruit rot with white growth",
                "bad smell from infected parts"
            ],
            "weather_conditions": ["cool temperature", "very high humidity", "prolonged wetness"],
            "severity": "very high",
            "treatment": [
                "Apply Metalaxyl + Mancozeb",
                "Immediate removal of infected plants",
                "Improve drainage",
                "Emergency fungicide application"
            ],
            "prevention": [
                "Use resistant varieties",
                "Avoid wet conditions",
                "Preventive fungicide sprays",
                "Good field drainage"
            ],
            "cost": "₹1000-1500 per acre treatment"
        }
    }
}

# ============================================
# AI DIAGNOSIS SYSTEM
# ============================================

def calculate_symptom_match(user_symptoms, disease_symptoms):
    """Calculate how well user symptoms match disease symptoms"""
    if not user_symptoms:
        return 0
    
    matches = 0
    for user_symptom in user_symptoms:
        for disease_symptom in disease_symptoms:
            if user_symptom.lower() in disease_symptom.lower() or disease_symptom.lower() in user_symptom.lower():
                matches += 1
                break
    
    # Return percentage match
    return (matches / len(user_symptoms)) * 100

def calculate_weather_match(user_weather, disease_weather):
    """Calculate how well weather conditions match"""
    if not user_weather:
        return 0
    
    matches = 0
    for user_condition in user_weather:
        for disease_condition in disease_weather:
            if user_condition.lower() in disease_condition.lower() or disease_condition.lower() in user_condition.lower():
                matches += 1
                break
    
    return (matches / len(user_weather)) * 100 if user_weather else 0

def diagnose_crop_disease(crop, symptoms, weather_conditions):
    """Main AI diagnosis function"""
    
    if crop not in crop_diseases:
        return {"error": f"Sorry, we don't have data for {crop} yet. Available crops: {list(crop_diseases.keys())}"}
    
    diagnosis_results = []
    
    for disease_key, disease_info in crop_diseases[crop].items():
        # Calculate symptom similarity
        symptom_score = calculate_symptom_match(symptoms, disease_info["symptoms"])
        
        # Calculate weather condition similarity
        weather_score = calculate_weather_match(weather_conditions, disease_info["weather_conditions"])
        
        # Calculate overall confidence (symptoms are more important than weather)
        confidence = (symptom_score * 0.7) + (weather_score * 0.3)
        
        diagnosis_results.append({
            "disease": disease_info["name"],
            "confidence": round(confidence, 1),
            "symptom_match": round(symptom_score, 1),
            "weather_match": round(weather_score, 1),
            "severity": disease_info["severity"],
            "treatment": disease_info["treatment"],
            "prevention": disease_info["prevention"],
            "cost": disease_info["cost"]
        })
    
    # Sort by confidence score
    diagnosis_results.sort(key=lambda x: x["confidence"], reverse=True)
    
    return {
        "crop": crop,
        "total_symptoms_checked": len(symptoms),
        "weather_conditions_checked": len(weather_conditions),
        "possible_diseases": diagnosis_results,
        "top_diagnosis": diagnosis_results[0] if diagnosis_results else None
    }

# ============================================
# TESTING THE SYSTEM
# ============================================

def test_diagnosis_system():
    """Test the diagnosis system with sample cases"""
    
    print("🌾 FarmAI Helper - Testing Diagnosis System")
    print("=" * 50)
    
    # Test Case 1: Rice Blast
    print("\n🧪 TEST 1: Rice with blast symptoms")
    symptoms1 = ["brown spots on leaves", "wilting", "white centers"]
    weather1 = ["high humidity", "cool nights"]
    result1 = diagnose_crop_disease("rice", symptoms1, weather1)
    
    print(f"Top diagnosis: {result1['top_diagnosis']['disease']}")
    print(f"Confidence: {result1['top_diagnosis']['confidence']}%")
    print(f"Treatment: {result1['top_diagnosis']['treatment'][0]}")
    
    # Test Case 2: Tomato Late Blight
    print("\n🧪 TEST 2: Tomato with late blight symptoms")
    symptoms2 = ["water-soaked dark spots", "white mold", "bad smell"]
    weather2 = ["cool temperature", "very high humidity"]
    result2 = diagnose_crop_disease("tomato", symptoms2, weather2)
    
    print(f"Top diagnosis: {result2['top_diagnosis']['disease']}")
    print(f"Confidence: {result2['top_diagnosis']['confidence']}%")
    print(f"Severity: {result2['top_diagnosis']['severity']}")
    
    # Test Case 3: Unknown symptoms
    print("\n🧪 TEST 3: Unusual symptoms")
    symptoms3 = ["purple leaves", "strange growth"]
    weather3 = ["normal weather"]
    result3 = diagnose_crop_disease("rice", symptoms3, weather3)
    
    print(f"Top diagnosis: {result3['top_diagnosis']['disease']}")
    print(f"Confidence: {result3['top_diagnosis']['confidence']}%")
    print("(Low confidence indicates unusual case)")

# ============================================
# INTERACTIVE DEMO FUNCTION
# ============================================

def interactive_diagnosis():
    """Interactive function for live demo during hackathon"""
    
    print("\n🌾 Welcome to FarmAI Helper!")
    print("Your AI-powered crop disease diagnosis system")
    print("=" * 50)
    
    # Get crop type
    available_crops = list(crop_diseases.keys())
    print(f"\nAvailable crops: {', '.join(available_crops)}")
    crop = input("Enter your crop type: ").lower().strip()
    
    if crop not in available_crops:
        print(f"Sorry, please choose from: {', '.join(available_crops)}")
        return
    
    # Get symptoms
    print(f"\nCommon symptoms for {crop}:")
    all_symptoms = set()
    for disease_info in crop_diseases[crop].values():
        all_symptoms.update(disease_info["symptoms"])
    
    for i, symptom in enumerate(list(all_symptoms)[:8], 1):
        print(f"{i}. {symptom}")
    
    print("\nDescribe the symptoms you see (separate by commas):")
    user_input = input("Symptoms: ")
    symptoms = [s.strip() for s in user_input.split(',') if s.strip()]
    
    # Get weather conditions
    print("\nRecent weather conditions (separate by commas):")
    print("Examples: high humidity, cool nights, heavy rain, drought")
    weather_input = input("Weather: ")
    weather_conditions = [w.strip() for w in weather_input.split(',') if w.strip()]
    
    # Diagnose
    result = diagnose_crop_disease(crop, symptoms, weather_conditions)
    
    # Display results
    print("\n" + "="*50)
    print("🎯 DIAGNOSIS RESULTS")
    print("="*50)
    
    if result["top_diagnosis"]["confidence"] > 60:
        print(f"✅ HIGH CONFIDENCE DIAGNOSIS")
    elif result["top_diagnosis"]["confidence"] > 30:
        print(f"⚠️  MODERATE CONFIDENCE DIAGNOSIS")
    else:
        print(f"❓ LOW CONFIDENCE - Unusual symptoms")
    
    top = result["top_diagnosis"]
    print(f"\n🦠 Disease: {top['disease']}")
    print(f"🎯 Confidence: {top['confidence']}%")
    print(f"⚡ Severity: {top['severity'].upper()}")
    print(f"💰 Treatment Cost: {top['cost']}")
    
    print(f"\n💊 RECOMMENDED TREATMENT:")
    for i, treatment in enumerate(top['treatment'], 1):
        print(f"{i}. {treatment}")
    
    print(f"\n🛡️ PREVENTION FOR FUTURE:")
    for i, prevention in enumerate(top['prevention'], 1):
        print(f"{i}. {prevention}")
    
    # Show alternative diagnoses
    if len(result["possible_diseases"]) > 1:
        print(f"\n📋 OTHER POSSIBLE DISEASES:")
        for disease in result["possible_diseases"][1:3]:  # Show top 2 alternatives
            print(f"• {disease['disease']} ({disease['confidence']}% confidence)")

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    print("🌾 FarmAI Helper - Crop Disease Diagnosis System")
    print("Developed for NextGen Hackathon 2025")
    print("="*60)
    
    while True:
        print("\nChoose an option:")
        print("1. Run test cases")
        print("2. Interactive diagnosis")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            test_diagnosis_system()
        elif choice == "2":
            interactive_diagnosis()
        elif choice == "3":
            print("Thanks for using FarmAI Helper! 🌾")
            break
        else:
            print("Please enter 1, 2, or 3")
