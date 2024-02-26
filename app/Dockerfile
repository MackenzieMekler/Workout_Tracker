FROM python:3.11

EXPOSE 8501 

WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy folders into the container
COPY pages /app/pages
COPY workout.py /app
COPY home.py /app
COPY templates /app/templates
COPY scripts /app/scripts
COPY config /app/config

# execute streamlit command
CMD streamlit run workout.py
