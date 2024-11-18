import streamlit as st
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        password="20260918",
        database="crud_new1"
    )
except mysql.connector.Error as err:
    print("Error: ", err)


mycursor = mydb.cursor()
# print("Connection Established")
# print(mysql.connector.__version__)

# Sidebar for selecting the form type
form_option = st.sidebar.selectbox("Select form", ("Create", "Read", "Update", "Delete"))

# Display the Web App Tittle
def main():
    st.title("CRUD Web App With MySQL and Streamlit")
main()

# Function to display the Create form
def create_form():
    st.subheader("Create Entry into MySQL Workbench")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Submit"):
        if name and email:
            sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
            val = (name, email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success(f"Form Submitted Successfully \nName: {name}\nEmail: {email}")
        else:
            st.error("Both name and email are required.")

def read_form():
    st.subheader("Read the Data from MySQL Workbench")
    mycursor.execute("SELECT * FROM users")
    result = mycursor.fetchall()
    for row in result:
        st.write(row)

def update_form():
    st.subheader("Update Record")
    id_number = st.number_input("Enter ID of the user you want to update")
    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Update"):
        sql = ("UPDATE users set name=%s, email=%s WHERE id=%s")
        val = (name, email, id_number)
        mycursor.execute(sql, val)
        mydb.commit()
        st.success(f"Records Updated Successfully \nName: {name}\nEmail: {email}")

def delete_form():
    st.subheader("Delete Record")
    id_number = st.number_input("Enter ID of the user you want to delete")

    if st.button("Delete"):
        sql = ("DELETE FROM users WHERE id=%s")
        val = (id_number,)
        mycursor.execute(sql, val)
        mydb.commit()
        st.success(f"Records Delete Successfully")

# Logic to call the appropriate form based on the sidebar selection
if form_option == "Create":
    create_form()
elif form_option == "Read":
    read_form()
elif form_option == "Update":
    update_form()
elif form_option == "Delete":
    delete_form()


# Establishing the connection with MySQL
# if the connection fails run the command below to try
# pip install --upgrade mysql-connector-python

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="20260918",
#     database="crud_new1"
# )



