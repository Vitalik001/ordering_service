FROM python:3.9

#
WORKDIR /code

#
COPY requirements.txt /code/fastapi_app/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/fastapi_app/requirements.txt

#
COPY . /code/fastapi_app

#
CMD ["uvicorn", "fastapi_app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/fastapi_app"]
