import pymysql
import  sqlalchemy as db
import pandas as pd

df = pd.read_csv("feedback_dataset_fr.csv")

with open ('./express/.env') as f:
    lines = f.readlines()
    for line in lines:
        if 'user' in line.lower():
          db_user = line.split('=')[1].strip()
        if 'password' in line.lower():
          db_password = line.split('=')[1].strip()
        if 'host' in line.lower():
          db_host = line.split('=')[1].strip()
        if 'name' in line.lower():
          db_name = line.split('=')[1].strip()
df["date"]=pd.to_datetime(df["date"])

# print(df.dtypes)

# Create a connection engine
engine = db.create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

# Create the 'feedback' table in the database
create_table_query ="""
Create Table if NOT EXISTS Users(
  ID INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

Create Table IF NOT EXISTS Employee(
  Name VARCHAR(255) PRIMARY KEY
  
);
Create Table IF NOT EXISTS Instructor(
  Name VARCHAR(255) PRIMARY KEY
);
Create Table IF NOT EXISTS Course(
  Name VARCHAR(255) PRIMARY KEY,
  
  Duration INT,
  Difficulty FLOAT
);

CREATE TABLE IF NOT EXISTS feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(255),
    instructor_name VARCHAR(255),
    knowledge_subject FLOAT,
    professionalism FLOAT,
    communication_skills FLOAT,
    engagement_participants FLOAT,
    answering_questions FLOAT,
    pacing_course FLOAT,
    overall_quality FLOAT,
    Date DATE,
    course_name VARCHAR(255),
    relevance_course FLOAT,
    clarity_objectives FLOAT,
    quality_materials FLOAT,
    depth_coverage FLOAT,
    usefulness_content FLOAT,
    text TEXT,
    experience_rating FLOAT,
    FOREIGN KEY (employee_name) REFERENCES Employee(Name),
    FOREIGN KEY (instructor_name) REFERENCES Instructor(Name),
    FOREIGN KEY (course_name) REFERENCES Course(Name)
);
"""
def get_subqueries(query):
  queries = query.split(';')
  return [q+';' for q in queries if q][:-1]


# Iterate on each row as a dictionary
with engine.connect() as connection:
  for _, row in df.iterrows():
    feedback_data = {
      'instructor_Name': row['instructor_Name'],
      'employee_Name': row['employee_Name'],
      
      'knowledge_subject': row['knowledge_subject'],
      'professionalism': row['professionalism'],
      'communication_skills': row['communication_skills'],
      'engagement_participants': row['engagement_participants'],
      'answering_questions': row['answering_questions'],
      'pacing_course': row['pacing_course'],
      'overall_quality': row['OverallScore'],
      
      'course_Name': row['course_Name'],
      'course_Duration': row['duration_hours'],
      'course_difficulty': row['difficulty'],
      
      'relevance_course': row['relevance_course'],
      'clarity_objectives': row['clarity_objectives'],
      'quality_materials': row['quality_materials'],
      'depth_coverage': row['depth_coverage'],
      'usefulness_content': row['usefulness_content'],
      
      'text': row['text_french'],
      
      'experience_rating': row['experience_rating']
    }
    insert_query=f"""INSERT IGNORE into instructor(Name) values('{feedback_data['instructor_Name']}');
              Insert IGNORE into Employee(Name) values('{feedback_data['employee_Name']}');
              Insert IGNORE into Course(Name,Duration,Difficulty) values('{feedback_data['course_Name']}',{feedback_data['course_Duration']},{feedback_data['course_difficulty']});
              Insert into feedback(employee_name,instructor_name,knowledge_subject,professionalism,communication_skills,engagement_participants,answering_questions,pacing_course,overall_quality,Date,course_name,relevance_course,clarity_objectives,quality_materials,depth_coverage,usefulness_content,text,experience_rating) 
              values("{feedback_data['employee_Name']}","{feedback_data['instructor_Name']}",{feedback_data['knowledge_subject']},{feedback_data['professionalism']},{feedback_data['communication_skills']},{feedback_data['engagement_participants']},{feedback_data['answering_questions']},{feedback_data['pacing_course']},{feedback_data['overall_quality']},'{row['date']}',"{feedback_data['course_Name']}",{feedback_data['relevance_course']},{feedback_data['clarity_objectives']},{feedback_data['quality_materials']},{feedback_data['depth_coverage']},{feedback_data['usefulness_content']},"{feedback_data['text']}",{feedback_data['experience_rating']});
            """

    
    for query in get_subqueries(create_table_query):
      connection.execute(db.text(query))
    for query in get_subqueries(insert_query):
      connection.execute(db.text(query))
      
connection.commit()  
