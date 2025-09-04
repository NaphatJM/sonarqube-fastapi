# FastAPI Application

FastAPI application สำหรับทดสอบ CI/CD pipeline ด้วย Jenkins, Docker และ SonarQube

## Features

- คำนวณค่าเฉลี่ยจากลิสต์ของตัวเลข
- กลับลำดับข้อความ
- API Documentation อัตโนมัติด้วย FastAPI
- Unit tests ด้วย pytest
- Code coverage reporting
- SonarQube integration
- Docker containerization

## Installation

### Local Development

1. Clone repository:
```bash
git clone <repository-url>
cd fastapi-app
```

2. สร้าง virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# หรือ
venv\Scripts\activate  # Windows
```

3. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

4. รันแอปพลิเคชัน:
```bash
uvicorn app.main:app --reload
```

แอปพลิเคชันจะรันที่ http://localhost:8000

### Docker

1. Build Docker image:
```bash
docker build -t fastapi-app .
```

2. รัน container:
```bash
docker run -p 8000:8000 fastapi-app
```

## API Endpoints

- `GET /` - Health check endpoint
- `GET /average?numbers=1&numbers=2&numbers=3` - คำนวณค่าเฉลี่ย
- `GET /reverse?text=hello` - กลับลำดับข้อความ
- `GET /docs` - API Documentation (Swagger UI)
- `GET /redoc` - API Documentation (ReDoc)

## Testing

รัน unit tests:
```bash
pytest
```

รัน tests พร้อม coverage:
```bash
pytest --cov=app --cov-report=html
```

## CI/CD Pipeline

โปรเจคนี้ใช้ Jenkins สำหรับ CI/CD pipeline ที่ประกอบด้วย:

1. **Checkout** - ดึงโค้ดจาก Git repository
2. **Install Dependencies** - ติดตั้ง Python packages
3. **Run Tests & Coverage** - รัน unit tests และสร้าง coverage report
4. **SonarQube Analysis** - วิเคราะห์คุณภาพโค้ด
5. **Build Docker Image** - สร้าง Docker image
6. **Deploy Container** - deploy container

## Project Structure

```
fastapi-app/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   └── utils.py         # Utility functions
├── test/
│   ├── __init__.py
│   ├── test_main.py     # API tests
│   └── test_utils.py    # Utility function tests
├── Dockerfile           # Docker configuration
├── Jenkinsfile         # Jenkins pipeline configuration
├── requirements.txt    # Python dependencies
├── pytest.ini         # Pytest configuration
├── sonar-project.properties  # SonarQube configuration
└── README.md           # Project documentation
```

## Configuration Files

- **Dockerfile**: สำหรับ containerization
- **Jenkinsfile**: Jenkins pipeline configuration
- **sonar-project.properties**: SonarQube analysis configuration
- **pytest.ini**: pytest configuration
- **requirements.txt**: Python dependencies

## Contributing

1. Fork the repository
2. สร้าง feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add some amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

This project is licensed under the MIT License.
