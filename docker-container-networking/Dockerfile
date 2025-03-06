FROM python:3.11

WORKDIR /app

# environment variable
ENV postgre_connect="Change_Me_to_Contianer_Ip"
ENV postgre_user="postgres"
ENV postgre_password="admin"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 3000

CMD [ "python3", "pytodb_con.py"]

