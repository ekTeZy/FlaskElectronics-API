# FlaskElectronics-API

**FlaskElectronics-API** — это RESTful API-сервис на Python с использованием Flask, который позволяет управлять продуктами, категориями и анализировать продажи.

Проект включает:\
**PostgreSQL + Alembic** для работы с БД.\
**Чистая архитектура**: **Repository -> Service -> API**.\
**Кэширование API** с автоматической очисткой.\
**Гибкое логирование для отладки и тестирования**.

---

## 1. Установка и запуск проекта

### **1.1. Клонирование репозитория**

```bash
git clone https://github.com/ТВОЙ_РЕПОЗИТОРИЙ/FlaskElectronics-API.git
cd FlaskElectronics-API
```

### **1.2. Создание виртуального окружения**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **1.3. Установка зависимостей**

```bash
pip install -r requirements.txt
```

### **1.4. Настройка переменных окружения**

Создай файл `.env` в корне проекта и добавь конфигурацию базы данных:

```ini
DATABASE_URL=postgresql://flask_user:123456@localhost/flask_electronic
```

### **1.5. Инициализация базы данных**

```bash
flask db upgrade
```

### **1.6. Запуск сервера**

```bash
flask run
```

---

## 2. Использование API

### **2.1. Получение списка продуктов**

```bash
curl -X GET "http://127.0.0.1:5000/api/products"
```

### **2.2. Получение общей суммы продаж за период**

```bash
curl -X GET "http://127.0.0.1:5000/api/sales/total?start_date=2024-09-19&end_date=2025-03-19"
```

### **2.3. Получение топ-N продаваемых товаров**

```bash
curl -X GET "http://127.0.0.1:5000/api/sales/top-products?start_date=2024-09-19&end_date=2025-03-19&limit=3"
```
