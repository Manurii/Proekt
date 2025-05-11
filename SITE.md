<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StudyBuddy - Органайзер навчання</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        :root {
            --primary-color: #4a6fa5;
            --secondary-color: #166088;
            --accent-color: #4fc3f7;
            --background-color: #f5f5f5;
            --text-color: #333333;
            --light-text: #ffffff;
            --dark-text: #212121;
        }
        body {
            font-family: 'Helvetica', Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            color: var(--text-color);
        }
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        header {
            background-color: var(--light-text);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
        }
        .logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logo img {
            height: 40px;
        }
        .logo h1 {
            color: var(--primary-color);
            margin: 0;
        }
        nav ul {
            display: flex;
            list-style: none;
            gap: 20px;
        }
        nav a {
            color: var(--text-color);
            text-decoration: none;
            font-weight: bold;
            padding: 5px 10px;
        }
        nav a:hover {
            color: var(--primary-color);
        }
        .active {
            color: var(--primary-color);
            border-bottom: 2px solid var(--primary-color);
        }
        .download-btn {
            background-color: var(--primary-color);
            color: white;
            padding: 8px 15px;
            border-radius: 5px;
        }
        .hero {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 120px 0 60px;
            margin-top: 70px;
        }
        .hero-container {
            display: flex;
            align-items: center;
            gap: 40px;
        }
        .hero-content {
            flex: 1;
        }
        .hero-image {
            flex: 1;
            text-align: center;
        }
        .hero-image img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .hero h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
        }
        .hero-buttons {
            display: flex;
            gap: 15px;
            margin-top: 30px;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
            text-decoration: none;
            cursor: pointer;
        }
        .primary {
            background-color: white;
            color: var(--primary-color);
        }
        .secondary {
            border: 2px solid white;
            color: white;
        }
        .features, .contact {
            padding: 80px 0;
        }
        .features h2, .contact h2 {
            text-align: center;
            color: var(--primary-color);
            font-size: 2rem;
            margin-bottom: 50px;
        }
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        .feature-card {
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }
        .feature-icon {
            font-size: 2.5rem;
            color: var(--primary-color);
            margin-bottom: 20px;
        }
        .feature-card h3 {
            color: var(--primary-color);
            margin-bottom: 15px;
        }
        .screenshot {
            margin-top: 20px;
            text-align: center;
        }
        .screenshot img {
            max-width: 100%;
            border-radius: 8px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            border: 1px solid #eee;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        .screenshot img:hover {
            transform: scale(1.02);
        }
        .contact-container {
            display: flex;
            flex-wrap: wrap;
            gap: 40px;
        }
        .contact-info, .contact-form {
            flex: 1 1 300px;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
        }
        .info-item {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }
        .social-links {
            display: flex;
            gap: 15px;
            margin-top: 30px;
        }
        .social-links a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background-color: var(--primary-color);
            color: white;
            border-radius: 50%;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        input, textarea {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-family: inherit;
        }
        textarea {
            min-height: 150px;
        }
        footer {
            background-color: var(--dark-text);
            color: white;
            padding: 60px 0 20px;
        }
        .footer-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
        }
        .footer-logo img {
            height: 40px;
        }
        .footer-links h4 {
            margin-bottom: 20px;
        }
        .footer-links ul {
            list-style: none;
            padding: 0;
        }
        .footer-links li {
            margin-bottom: 10px;
        }
        .footer-links a {
            color: white;
            text-decoration: none;
        }
        .copyright {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }

        /* Модальное окно для скриншотов */
        .modal {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
            overflow: auto;
        }
        .modal-content {
            display: flex;
            flex-direction: column;
            background-color: #fff;
            margin: 5% auto;
            padding: 20px;
            border-radius: 10px;
            width: 80%;
            max-width: 800px;
            box-shadow: 0 5px 30px rgba(0,0,0,0.3);
            animation: modalopen 0.5s;
        }
        @keyframes modalopen {
            from {opacity: 0; transform: scale(0.8);}
            to {opacity: 1; transform: scale(1);}
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .modal-header h3 {
            margin: 0;
            color: var(--primary-color);
        }
        .close {
            color: #aaa;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }
        .close:hover {
            color: #333;
        }
        .modal-body {
            text-align: center;
        }
        .modal-body img {
            max-width: 100%;
            max-height: 70vh;
            border-radius: 5px;
            border: 1px solid #ddd;
        }

        @media (max-width: 768px) {
            .hero-container, .contact-container {
                flex-direction: column;
            }
            nav ul {
                display: none;
            }
            .modal-content {
                width: 95%;
                margin: 10% auto;
            }
        }
    </style>
</head>
<body id="top">
    <header>
        <div class="container header-container">
            <nav>
                <ul>
                    <li><a href="#top" class="active">Головна</a></li>
                    <li><a href="#features">Опис програми</a></li>
                    <li><a href="#contact">Контакти</a></li>
                    <li><a href="#download" class="download-btn">Завантажити</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container hero-container">
            <div class="hero-content">
                <h2>Організуй своє навчання з StudyBuddy</h2>
                <p>StudyBuddy допоможе організувати навчальний процес, контролювати завдання та слідкувати за успішністю.</p>
                <div class="hero-buttons">
                    <a href="#download" class="btn primary">Завантажити</a>
                    <a href="#features" class="btn secondary">Дізнатись більше</a>
                </div>
            </div>
            <div class="hero-image">
                <img src="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80" alt="StudyBuddy додаток">
            </div>
        </div>
    </section>

    <section id="features" class="features">
        <div class="container">
            <h2>Можливості StudyBuddy</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-calendar-alt"></i>
                    </div>
                    <h3>Розклад занять</h3>
                    <p>Інтуїтивно зрозумілий календар з розкладом твоїх занять на день, тиждень чи місяць. Додавай заняття, вказуй аудиторії та викладачів.</p>
                    <div class="screenshot">
        <img src="https://i.ibb.co/W4tS2QRr/schedule-screen.png"
             alt="Розклад занять"
             onclick="openModal('Розклад занять', 'https://i.ibb.co/W4tS2QRr/schedule-screen.png')">                    </div>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-tasks"></i>
                    </div>
                    <h3>Домашні завдання</h3>
                    <p>Створюй список завдань з термінами виконання, пріоритетами та категоріями. Отримуй нагадування про наближення дедлайнів.</p>
                    <div class="screenshot">
        <img src="https://i.ibb.co/1fd1m8XV/tasks-screen.png"
             alt="Домашні завдання"
             onclick="openModal('Домашні завдання', 'https://i.ibb.co/1fd1m8XV/tasks-screen.png')">                    </div>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h3>Контроль успішності</h3>
                    <p>Відстежуй свої оцінки з усіх предметів. Аналізуй прогрес у навчанні за допомогою наочних графіків та статистики.</p>
                    <div class="screenshot">
        <img src="https://i.ibb.co/7fmJrX2/grades-screen.png"
             alt="Контроль успішності"
             onclick="openModal('Контроль успішності', 'https://i.ibb.co/7fmJrX2/grades-screen.png')">                            </div>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-bell"></i>
                    </div>
                    <h3>Нагадування</h3>
                    <p>Ніколи не пропускай важливі події чи дедлайни завдань. Налаштовуй сповіщення за кілька днів або годин до події.</p>
                    <div class="screenshot">
        <img src="https://i.ibb.co/FbDgNf5y/reminders-screen.png"
             alt="Нагадування"
             onclick="openModal('Нагадування','https://i.ibb.co/FbDgNf5y/reminders-screen.png')">
                    </div>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-book"></i>
                    </div>
                    <h3>Навчальні матеріали</h3>
                    <p>Зберігай всі необхідні матеріали в одному місці. Організовуй файли за предметами та темами для швидкого доступу.</p>

                </div>

                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-mobile-alt"></i>
                    </div>
                    <h3>Доступ з будь-якого пристрою</h3>
                    <p>Працюй зі своїми даними на комп'ютері, планшеті чи смартфоні. Твої дані синхронізуються між усіма пристроями.</p>

                </div>
            </div>
        </div>
    </section>

    <section id="contact" class="contact">
        <div class="container">
            <h2>Зв'яжіться з нами</h2>
            <div class="contact-container">
                <div class="contact-info">
                    <div class="info-item">
                        <i class="fas fa-envelope"></i>
                        <p>support@studybuddy.com</p>
                    </div>
                    <div class="info-item">
                        <i class="fas fa-phone"></i>
                        <p>+380 66 822 8770</p>
                    </div>
                    <div class="info-item">
                        <i class="fas fa-map-marker-alt"></i>
                        <p>м. Чернігів вул.Козацька 28, 15</p>
                    </div>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                <div class="contact-form">
                    <form>
                        <input type="text" placeholder="Ваше ім'я" required>
                        <input type="email" placeholder="Ваш email" required>
                        <textarea placeholder="Ваше повідомлення" required></textarea>
                        <button type="submit" class="btn primary">Надіслати</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <section id="download" class="features">
        <div class="container">
            <h2>Завантажити StudyBuddy</h2>
            <p style="text-align: center;">
                <a href="https://drive.google.com/uc?export=download&id=1hgxWF6-dzfSII8FFtScYOqOAlGZadk_A" download class="btn primary">
                    Скачати StudyBuddy (.exe)
                </a>
            </p>
            <div style="text-align: center; margin-top: 30px;">
                <h3>Системні вимоги</h3>
                <p>Windows 10/11 (64-bit) | macOS 10.15+ | 2GB RAM | 200MB вільного місця</p>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="footer-container">

                <div class="footer-links">
                    <h4>Меню</h4>
                    <ul>
                        <li><a href="#top">Головна</a></li>
                        <li><a href="#features">Опис програми</a></li>
                        <li><a href="#contact">Контакти</a></li>
                        <li><a href="#download">Завантажити</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Підтримка</h4>
                    <ul>
                        <li><a href="#">FAQ</a></li>
                        <li><a href="#">Довідка</a></li>
                        <li><a href="#">Політика конфіденційності</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Ресурси</h4>
                    <ul>
                        <li><a href="#">Інструкція з використання</a></li>
                        <li><a href="#">Оновлення</a></li>
                        <li><a href="#">Блог</a></li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2025 StudyBuddy. Всі права захищені.</p>
            </div>
        </div>
    </footer>

    <!-- Модальное окно для скриншотов -->
    <div id="screenshotModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modalTitle">Заголовок</h3>
                <span class="close">&times;</span>
            </div>
            <div class="modal-body">
                <img id="modalImage" src="" alt="Скриншот">
            </div>
        </div>
    </div>

    <script>
        // Функция для открытия модального окна с скриншотом
        function openModal(title, imageSrc) {
            const modal = document.getElementById('screenshotModal');
            const modalTitle = document.getElementById('modalTitle');
            const modalImage = document.getElementById('modalImage');

            modalTitle.textContent = title;
            modalImage.src = imageSrc;
            modal.style.display = 'block';

            // Закрытие при клике на крестик
            document.querySelector('.close').onclick = function() {
                modal.style.display = 'none';
            }

            // Закрытие при клике вне модального окна
            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = 'none';
                }
            }
        }

        // Плавная прокрутка для якорных ссылок
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });

        // Обработка формы
        document.querySelector('form').addEventListener('submit', function (e) {
            e.preventDefault();
            const name = this.querySelector('input[type="text"]').value;
            const email = this.querySelector('input[type="email"]').value;
            const message = this.querySelector('textarea').value;

            if (name && email && message) {
                alert(`Дякуємо, ${name}! Ваше повідомлення надіслано.`);
                this.reset();
            } else {
                alert('Будь ласка, заповніть усі поля.');
            }
        });
    </script>
</body>
</html>
