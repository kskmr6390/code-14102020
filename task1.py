
import os
import json
from dotenv import load_dotenv


def GetBMIcategoriesAndHealthRisk(BMI):

  if  BMI <= 18.4:
    BMI_category = "Underweight"
    Health_risk ='low Risk'
  
  elif BMI >= 18.5 and BMI <=24.9:
    BMI_category="Normal weight"
    Health_risk='Low Risk'
  
  elif BMI >=25 and BMI <=29.9:
    BMI_category="Overweight"
    Health_risk='Enhanched risk'
   
  elif BMI >=30 and BMI <=34.9:
    BMI_category="Moderately obese"
    Health_risk='Medium risk'
    
   
  elif BMI >=35 and BMI <=39.9:
    BMI_category="Severely obese"
    Health_risk='High risk'
   
  elif BMI >= 40:
    BMI_category="Very severely obese"
    Health_risk='Very High risk'
   
  return BMI_category,Health_risk

def GetBMIDetails(Data):
  TempData=Data
  for person  in TempData:
    bmi=person['WeightKg']/((person['HeightCm']/100)*(person['HeightCm']/100))
    #print("Your BMI is:",bmi)
    BMI_category,Health_risk=GetBMIcategoriesAndHealthRisk(bmi)
    person['BMI_Score']=bmi
    person['BMI_Category']=BMI_category
    person['Health_risk']=Health_risk
  return TempData
  
def GetOverweightCount(result):
  overweightcount=0
  for Record in result:
    if Record['BMI_Category']=='Overweight':
      overweightcount +=1
  return overweightcount

#driverfunction

#load  env variables
load_dotenv()
#DataPath=""
DataPath=os.environ.get("DataPath")
print(DataPath)
with open(DataPath) as file:
  data = json.load(file)
#print(data)

#function call for BMI Details 
result=GetBMIDetails(data)
# overweight count  function call
OverweightCount=GetOverweightCount(result)
print("Total count of OverWeight people  is:",OverweightCount)

print("Here is BMI Details of  each records:-")
for person in result:
 print(person)
