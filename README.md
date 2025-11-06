# 🍽️ Restaurant Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)](https://www.postgresql.org/)

> A comprehensive dashboard application for restaurant management, featuring menu, orders, recipes, and real-time inventory tracking.

## ✨ Features

### 🔐 User Authentication
- JWT-based secure authentication
- Role-based access control
- Session management

### 📊 Dashboard Overview
- Real-time performance metrics
- Key performance indicators (KPIs)
- Quick access navigation
- Live data updates

### 📋 Menu Management
- Create and edit menu items
- Category organization
- Price management
- Item availability tracking

### 📦 Inventory Management
- Real-time stock level tracking
- Low stock alerts
- Transaction history
- Supplier management

### 🛒 Order Processing
- End-to-end order management
- Order creation and tracking
- Status updates (Pending → Preparing → Ready → Completed)
- Sales reporting and analytics

### 📖 Recipe Management
- Recipe creation and editing
- Ingredient-menu item linking
- Automated cost calculation
- Recipe-inventory integration

## 🏗️ Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Material-UI** - Professional component library
- **React Router** - Client-side routing
- **Axios** - HTTP client

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - ORM for database operations
- **JWT** - Secure authentication
- **Flask-CORS** - Cross-origin resource sharing

### Database
- **PostgreSQL 12+** - Relational database
- ACID compliance
- Data integrity constraints

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v14 or higher)
- **Python** (v3.8 or higher)
- **PostgreSQL** (v12 or higher)
- **pnpm** (or npm/yarn)

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/restaurant-management-system.git
cd restaurant-management-system
```

#### 2. Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Start the Flask server
python main.py
```

The backend API will run on `http://localhost:5000`

#### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend/restaurant-dashboard

# Install dependencies
pnpm install

# Start the development server
pnpm run dev
```

The frontend will run on `http://localhost:5173`

### Demo Credentials

```
Username: admin
Password: admin123
```

## 📁 Project Structure

```
restaurant-management-system/
├── backend/
│   ├── main.py              # Flask application entry point
│   ├── init_db.py           # Database initialization script
│   ├── requirements.txt     # Python dependencies
│   ├── models/              # SQLAlchemy models
│   ├── routes/              # API endpoints
│   └── utils/               # Helper functions
├── frontend/
│   └── restaurant-dashboard/
│       ├── src/
│       │   ├── components/  # React components
│       │   ├── pages/       # Page components
│       │   ├── services/    # API services
│       │   └── App.jsx      # Main App component
│       ├── package.json
│       └── vite.config.js
└── README.md
```

## 🔧 Configuration

### Backend Configuration

Create a `.env` file in the backend directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/restaurant_db
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key
```

### Frontend Configuration

Create a `.env` file in the frontend directory:

```env
VITE_API_URL=http://localhost:5000
```

## 📊 Database Schema

The system uses a relational database with the following main tables:

- **users** - User accounts and authentication
- **menu_items** - Menu items with categories and pricing
- **inventory** - Stock levels and inventory tracking
- **orders** - Customer orders and order history
- **recipes** - Recipe definitions and ingredient mapping
- **order_items** - Line items for each order

## 🔐 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `POST /api/auth/logout` - User logout

### Menu Management
- `GET /api/menu-items` - List all menu items
- `POST /api/menu-items` - Create new menu item
- `PUT /api/menu-items/:id` - Update menu item
- `DELETE /api/menu-items/:id` - Delete menu item

### Inventory
- `GET /api/inventory` - List inventory items
- `POST /api/inventory` - Add inventory item
- `PUT /api/inventory/:id` - Update inventory
- `GET /api/inventory/alerts` - Get low stock alerts

### Orders
- `GET /api/orders` - List all orders
- `POST /api/orders` - Create new order
- `PUT /api/orders/:id` - Update order status
- `GET /api/orders/report` - Generate sales report

### Recipes
- `GET /api/recipes` - List all recipes
- `POST /api/recipes` - Create new recipe
- `PUT /api/recipes/:id` - Update recipe
- `DELETE /api/recipes/:id` - Delete recipe

## 🎯 Key Highlights

✅ **Centralized Management** - Single dashboard for all operations  
✅ **Real-time Tracking** - Live inventory and order updates  
✅ **Automated Calculations** - Recipe costs and profit margins  
✅ **Smart Alerts** - Low stock notifications  
✅ **Professional UI** - Modern, responsive design with Material-UI  
✅ **Secure** - JWT authentication and role-based access  
✅ **Scalable** - Built with industry-standard technologies  

## 🚧 Future Enhancements

- 📱 Mobile app for servers and kitchen staff
- 💳 POS system integration
- 🎁 Customer loyalty program
- 📈 Advanced analytics and reporting
- 🌍 Multi-location support
- 🔔 Push notifications for orders
- 📧 Email notifications for alerts
- 📱 QR code based table ordering

## 📝 Project Statistics

- **8 Development Phases** - Systematic approach from analysis to deployment
- **15+ Features** - Comprehensive restaurant management features
- **100% Completion** - Fully functional and deployed
- **Full-Stack Implementation** - React + Flask + PostgreSQL

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ankit Rajput**

A passionate full-stack developer crafting scalable and efficient solutions for real-world problems.

---

⭐ **Made with ❤️ by Ankit Rajput** ⭐

*If you find this project helpful, please consider giving it a star!*

---

## 📞 Contact & Connect

- 💼 GitHub: [@ankitrajput](https://github.com/ankitrajput)
- 📧 Email: contact@ankitrajput.dev
- 🌐 Portfolio: [ankitrajput.dev](https://ankitrajput.dev)

---

**#RestaurantManagement #FullStackDevelopment #ReactJS #Flask #PostgreSQL**
