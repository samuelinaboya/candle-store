# 🕯️ Candle Store

A beautiful, modern e-commerce web application for browsing and purchasing premium candles. Built with Flask, this project showcases a full product catalog with individual product pages and a checkout experience.

## ✨ Features

- **Home Page**: Browse all available candles with product previews
- **Product Pages**: View detailed information about each candle, including descriptions and characteristics
- **Checkout Page**: Complete the purchase process with a checkout form
- **Responsive Design**: Modern, clean UI built with HTML and CSS
- **Mock Database**: Pre-loaded product inventory with three premium candle options:
  - Eucalyptus Stack 7 OZ Candle ($28.00)
  - Sandalwood Stack 7 OZ Candle ($32.00)
  - Golden Mandarin Stack 7 OZ Candle ($28.00)

## 🛠️ Tech Stack

- **Backend**: Python 3.12 with Flask 3.1.3
- **Web Server**: Gunicorn 24.1.1
- **Frontend**: HTML, CSS
- **Deployment**: Docker

## 📁 Project Structure

```
candle-store/
├── app.py                 # Flask application with routes
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .dockerignore         # Docker ignore file
├── templates/            # Jinja2 HTML templates
│   ├── base.html        # Base template (layout)
│   ├── home.html        # Homepage with product listing
│   ├── product.html     # Individual product detail page
│   └── checkout.html    # Checkout/purchase page
├── static/              # Static assets
│   └── images/          # Product images
└── __pycache__/         # Python cache (auto-generated)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samuelinaboya/candle-store.git
   cd candle-store
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

```bash
python app.py
```

The application will start on `http://localhost:8080`

### Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t candle-store .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8080:8080 candle-store
   ```

The application will be available at `http://localhost:8080`

## 📋 Available Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page with product catalog |
| `/product/<id>` | GET | Individual product detail page |
| `/checkout` | GET | Checkout/purchase page |

### Product IDs

- `eucalyptus` - Eucalyptus Stack 7 OZ Candle
- `sandalwood` - Sandalwood Stack 7 OZ Candle
- `golden-mandarin` - Golden Mandarin Stack 7 OZ Candle

## 📦 Dependencies

- **Flask** (3.1.3): Python web framework for building the application
- **Gunicorn** (24.1.1): WSGI HTTP server for production deployment

## 🐳 Docker Information

The Dockerfile uses Python 3.12-slim as the base image and:
- Sets environment variables for Python optimization
- Installs dependencies from requirements.txt
- Exposes port 8080
- Runs the application with Gunicorn on startup

## 🎨 Language Composition

- **HTML**: 93.9%
- **Python**: 5.3%
- **Dockerfile**: 0.8%

## 📝 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 👤 Author

[Samuel Inaboya](https://github.com/samuelinaboya)

---

**Enjoy browsing our premium candle collection!** 🕯️✨
