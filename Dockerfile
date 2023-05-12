FROM python:3.9-alpine
WORKDIR /digigold
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /digigold
ENV SECRETKEY='django-insecure-2wk_l##n_mj7%qpr_p&(jy+6i=15u_!ao3o5@uj73nur@yu#2b'
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV EXTERNALIP='34.16.139.34'
RUN python3 manage.py collectstatic 
EXPOSE 8000
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]