# 🍽️ Restaurant Management System

[![Project Status](https://img.shields.io/badge/Status-Completed-success.svg)](https://github.com)
[![Tech Stack](https://img.shields.io/badge/Stack-React%20%7C%20Flask%20%7C%20PostgreSQL-blue.svg)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **A comprehensive dashboard application designed to streamline restaurant operations through integrated management of menus, inventory, orders, and recipes.**

![Restaurant Management System](https://img.shields.io/badge/Restaurant-Management-orange?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTExIDkgSDkgVjIgSDcgVjkgSDUgVjExIEg3IFYxNSBMOS41IDIwIEwxMiAxNSBWMTEgSDE0IFY5IEgxMiBWMiBIMTEgVjkgWiIvPjwvc3ZnPg==)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🎯 Overview

The **Restaurant Management System** is a full-stack web application that provides restaurant owners and managers with a powerful, centralized platform to manage all aspects of their business operations.

### 🎪 Key Benefits

✅ **Centralized Management** - Single dashboard for all operations  
✅ **Real-time Tracking** - Live inventory and order updates  
✅ **Automated Calculations** - Smart cost analysis and pricing  
✅ **Streamlined Workflow** - Efficient order processing  
✅ **Recipe Integration** - Link recipes with inventory management  

### 📊 Project Statistics

- **8** Development Phases
- **15+** Features Implemented
- **100%** Project Completion
- **Live Deployment** Ready

---

## ✨ Features

### 🔐 User Authentication
- JWT-based secure authentication
- Role-based access control
- Session management

### 📊 Dashboard Overview
- Real-time KPIs and metrics
- Quick navigation access
- Live data updates

### 📝 Menu Management
- Create and edit menu items
- Category organization
- Price management
- Menu item availability toggle

### 📦 Inventory Management
- Real-time stock level tracking
- Low stock alerts
- Transaction history
- Stock in/out management

### 🛒 Order Processing
- Order creation and tracking
- Status updates (Pending → Completed)
- Sales reporting
- Order history

### 📖 Recipe Management
- Recipe creation and editing
- Link recipes to menu items
- Automatic ingredient cost calculation
- Recipe-inventory integration

---

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Material-UI (MUI)** - Component library
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Vite** - Build tool

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - ORM
- **JWT** - Authentication
- **Flask-CORS** - Cross-origin support
- **PostgreSQL Driver** - Database connectivity

### Database
- **PostgreSQL 12+** - Relational database
- **ACID Compliance** - Data integrity
- **Relational Schema** - Normalized structure

---

## 🏗️ System Architecture

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│                 │         │                 │         │                 │
│  React Frontend │◄───────►│  Flask Backend  │◄───────►│   PostgreSQL    │
│                 │  REST   │                 │  SQL    │                 │
│  (Port 5173)    │   API   │  (Port 5000)    │ Queries │   Database      │
│                 │         │                 │         │                 │
└─────────────────┘         └─────────────────┘         └─────────────────┘
        │                           │
        │                           │
        ├─ Material-UI              ├─ SQLAlchemy ORM
        ├─ React Router             ├─ JWT Auth
        ├─ Axios                    ├─ Flask-CORS
        └─ State Management         └─ RESTful Endpoints
```

### 🔄 Data Flow

1. User interacts with React frontend
2. Axios sends HTTP requests to Flask API
3. Flask processes requests with business logic
4. SQLAlchemy queries PostgreSQL database
5. Data flows back through the stack
6. React updates UI with new data

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 12+
- pnpm (or npm)

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/ankitrajput0096/restaurant-management-system.git
cd restaurant-management-system

# Install Python dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Run the Flask server
python main.py
```

Backend will start at `http://localhost:5000`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend/restaurant-dashboard

# Install dependencies
pnpm install

# Start development server
pnpm run dev
```

Frontend will start at `http://localhost:5173`

### Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/restaurant_db
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key
FLASK_ENV=development
```

---

## 💻 Usage

### Demo Credentials

```
Username: admin
Password: admin123
```

### Live Application

- **Frontend**: [Live Demo](https://5173-ihf1tgn1j3imi7t79xr1d-e07d9c32.manusvm.computer)
- **Backend API**: [API Endpoint](https://5000-ihf1tgn1j3imi7t79xr1d-e07d9c32.manusvm.computer)

### Quick Start Guide

1. **Login** - Use demo credentials or create a new account
2. **Dashboard** - View key metrics and quick actions
3. **Menu** - Add/edit menu items with categories
4. **Inventory** - Track stock levels and get alerts
5. **Orders** - Create and manage customer orders
6. **Recipes** - Link recipes with automatic cost calculation

---

## 📡 API Documentation

### Authentication

```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

### Menu Items

```http
GET    /api/menu-items       # Get all menu items
POST   /api/menu-items       # Create new menu item
PUT    /api/menu-items/:id   # Update menu item
DELETE /api/menu-items/:id   # Delete menu item
```

### Inventory

```http
GET    /api/inventory        # Get all inventory items
POST   /api/inventory        # Add inventory item
PUT    /api/inventory/:id    # Update stock level
DELETE /api/inventory/:id    # Remove inventory item
```

### Orders

```http
GET    /api/orders           # Get all orders
POST   /api/orders           # Create new order
PUT    /api/orders/:id       # Update order status
DELETE /api/orders/:id       # Cancel order
```

### Recipes

```http
GET    /api/recipes          # Get all recipes
POST   /api/recipes          # Create new recipe
PUT    /api/recipes/:id      # Update recipe
DELETE /api/recipes/:id      # Delete recipe
```

---

## 📸 Screenshots

### Dashboard
![Dashboard Overview](https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=Dashboard+Overview)

### Menu Management
![Menu Management](https://via.placeholder.com/800x400/50C878/FFFFFF?text=Menu+Management)

### Inventory Tracking
![Inventory](https://via.placeholder.com/800x400/FF6B6B/FFFFFF?text=Inventory+Tracking)

### Order Processing
![Orders](https://via.placeholder.com/800x400/9B59B6/FFFFFF?text=Order+Processing)

---

## 🔮 Future Enhancements

- 📱 **Mobile App** - Native apps for servers and kitchen staff
- 💳 **POS Integration** - Direct point-of-sale system integration
- 🎁 **Loyalty Program** - Customer rewards and loyalty tracking
- 📊 **Advanced Analytics** - Detailed reports and insights
- 🌐 **Multi-location** - Support for restaurant chains
- 🔔 **Real-time Notifications** - WebSocket-based updates
- 🖨️ **Print Integration** - Kitchen printer support
- 📧 **Email Reports** - Automated daily/weekly reports

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use ESLint configuration for JavaScript/React
- Write meaningful commit messages
- Add comments for complex logic

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

### **Ankit Rajput**

> *Full Stack Developer | Open Source Enthusiast | Restaurant Tech Solutions*

[![GitHub](https://img.shields.io/badge/GitHub-ankitrajput0096-181717?style=for-the-badge&logo=github)](https://github.com/ankitrajput0096)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ankit%20Rajput-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/ankitrajput0096)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:ankitrajput0096@gmail.com)

**💼 Skills**: React • Flask • PostgreSQL • Python • JavaScript • Full Stack Development

**🌟 Passion**: Building scalable solutions that solve real-world problems

---

## 🙏 Acknowledgments

- React community for excellent documentation
- Flask team for the amazing framework
- Material-UI for beautiful components
- All contributors and testers

---

<div align="center">

### ⭐ If you find this project helpful, please give it a star!

**Made with ❤️ by Ankit Rajput**

© 2025 Restaurant Management System. All Rights Reserved.

</div>
