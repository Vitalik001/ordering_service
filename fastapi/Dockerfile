FROM python:3.9

#
WORKDIR /code/fastapi

#
COPY requirements.txt /code/fastapi/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/fastapi/requirements.txt

#
COPY . /code/fastapi

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/fastapi"]
