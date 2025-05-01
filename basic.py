import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import calendar
from datetime import datetime, timedelta
#from PIL import Image, ImageTk
import random

# Кольорова схема
COLORS = {
    'primary': '#4a6fa5',
    'secondary': 'SkyBlue2',
    'accent': '#4fc3f7',
    'background': '#f5f5f5',
    'text': '#333333',
    'success': '#4caf50',
    'warning': '#ff9800',
    'error': '#f44336',
    'light': '#ffffff',
    'dark': '#212121'
}

# Шрифти
FONTS = {
    'title': ('Helvetica', 16, 'bold'),
    'subtitle': ('Helvetica', 12, 'bold'),
    'regular': ('Helvetica', 10),
    'small': ('Helvetica', 8)
}


class StudyBuddyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("StudyBuddy - Органайзер навчання")
        self.root.geometry("1000x700")
        self.root.configure(bg=COLORS['background'])

        # Заглушка для логотипу
        self.logo_img = tk.PhotoImage(width=40, height=40)

        # Приклад даних
        self.subjects = ["Математика", "Фізика", "Історія", "Англійська", "Хімія"]
        self.tasks = [
            {"subject": "Математика", "task": "Домашнє завдання #5", "due": "15.05.2023", "status": "Активне",
             "priority": "Високий"},
            {"subject": "Історія", "task": "Підготувати презентацію", "due": "12.05.2023", "status": "Виконано",
             "priority": "Середній"},
            {"subject": "Англійська", "task": "Читання тексту", "due": "10.05.2023", "status": "Протерміновано",
             "priority": "Низький"}
        ]
        self.grades = [
            {"subject": "Математика", "date": "01.05.2023", "type": "Контрольна", "grade": "10", "comment": "Добре"},
            {"subject": "Фізика", "date": "03.05.2023", "type": "Лабораторна", "grade": "8", "comment": "Можна краще"},
            {"subject": "Історія", "date": "05.05.2023", "type": "Тест", "grade": "9", "comment": ""}
        ]

        self.setup_ui()
        self.show_home_page()  # Показуємо головну сторінку при запуску

    def setup_ui(self):
        # Верхня панель з лого та назвою
        self.header_frame = tk.Frame(self.root, bg=COLORS['primary'])
        self.header_frame.pack(fill='x', padx=10, pady=10)

        self.logo_label = tk.Label(self.header_frame, image=self.logo_img, bg=COLORS['primary'])
        self.logo_label.pack(side='left', padx=10)

        self.title_label = tk.Label(
            self.header_frame,
            text="StudyBuddy",
            font=FONTS['title'],
            fg=COLORS['light'],
            bg=COLORS['primary']
        )
        self.title_label.pack(side='left')

        # Панель навігації
        self.nav_frame = tk.Frame(self.root, bg=COLORS['secondary'])
        self.nav_frame.pack(fill='x', padx=10, pady=(0, 10))

        self.nav_buttons = []
        nav_items = [
            ("Головна", self.show_home_page),
            ("Розклад", self.show_schedule),
            ("Завдання", self.show_tasks),
            ("Оцінки", self.show_grades),
            ("Статистика", self.show_stats)
        ]

        for text, command in nav_items:
            btn = tk.Button(
                self.nav_frame,
                text=text,
                command=command,
                bg=COLORS['secondary'],
                fg=['SteelBlue'],
                activebackground=COLORS['accent'],
                activeforeground=COLORS['dark'],
                relief='flat',
                font=FONTS['subtitle'],
                padx=15,
                pady=5
            )
            btn.pack(side='left', padx=5)
            self.nav_buttons.append(btn)

        # Основна область контенту
        self.main_frame = tk.Frame(self.root, bg=COLORS['background'])
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))

        # Статус бар
        self.status_bar = tk.Label(
            self.root,
            text="Навчайся щодня - зростай назавжди!",
            bd=1,
            relief='sunken',
            anchor='w',
            font=FONTS['small'],
            bg=COLORS['light'],
            fg=COLORS['dark']
        )
        self.status_bar.pack(fill='x', padx=10, pady=(0, 10))

    def show_home_page(self):
        self.clear_main_frame()

        # Заголовок
        tk.Label(
            self.main_frame,
            text="Ласкаво просимо до StudyBuddy!",
            font=FONTS['title'],
            bg=COLORS['background'],
            fg=COLORS['primary']
        ).pack(pady=20)

        # Картки з інформацією
        cards_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        cards_frame.pack(fill='x', padx=20, pady=10)

        # Картка з активними завданнями
        active_tasks_card = tk.Frame(
            cards_frame,
            bg=COLORS['light'],
            relief='groove',
            bd=2,
            padx=10,
            pady=10
        )
        active_tasks_card.pack(side='left', fill='both', expand=True, padx=5)

        tk.Label(
            active_tasks_card,
            text="Активні завдання",
            font=FONTS['subtitle'],
            bg=COLORS['light'],
            fg=COLORS['primary']
        ).pack(anchor='w')

        active_count = len([t for t in self.tasks if t['status'] == 'Активне'])
        tk.Label(
            active_tasks_card,
            text=f"У вас {active_count} активних завдань",
            font=FONTS['regular'],
            bg=COLORS['light'],
            fg=COLORS['dark']
        ).pack(anchor='w', pady=5)

        # Картка з навчальним прогресом
        progress_card = tk.Frame(
            cards_frame,
            bg=COLORS['light'],
            relief='groove',
            bd=2,
            padx=10,
            pady=10
        )
        progress_card.pack(side='left', fill='both', expand=True, padx=5)

        tk.Label(
            progress_card,
            text="Навчальний прогрес",
            font=FONTS['subtitle'],
            bg=COLORS['light'],
            fg=COLORS['primary']
        ).pack(anchor='w')

        avg_grade = sum(int(g['grade']) for g in self.grades) / len(self.grades) if self.grades else 0
        tk.Label(
            progress_card,
            text=f"Середній бал: {avg_grade:.1f}",
            font=FONTS['regular'],
            bg=COLORS['light'],
            fg=COLORS['dark']
        ).pack(anchor='w', pady=5)

        # Найближчі події
        events_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        events_frame.pack(fill='both', expand=True, padx=20, pady=10)

        events_card = tk.Frame(
            events_frame,
            bg=COLORS['light'],
            relief='groove',
            bd=2,
            padx=10,
            pady=10
        )
        events_card.pack(fill='both', expand=True)

        tk.Label(
            events_card,
            text="Найближчі події",
            font=FONTS['subtitle'],
            bg=COLORS['light'],
            fg=COLORS['primary']
        ).pack(anchor='w')

        # Приклад подій
        events = [
            {"date": "12.05.2023", "event": "Контрольна з математики"},
            {"date": "15.05.2023", "event": "Здати домашнє завдання"},
            {"date": "18.05.2023", "event": "Презентація з історії"}
        ]

        for event in events:
            event_frame = tk.Frame(events_card, bg=COLORS['light'])
            event_frame.pack(fill='x', pady=2)

            tk.Label(
                event_frame,
                text=event['date'],
                font=FONTS['regular'],
                bg=COLORS['light'],
                fg=COLORS['dark'],
                width=10
            ).pack(side='left')

            tk.Label(
                event_frame,
                text=event['event'],
                font=FONTS['regular'],
                bg=COLORS['light'],
                fg=COLORS['dark']
            ).pack(side='left')

        # Кнопка швидкого додавання
        quick_add_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        quick_add_frame.pack(fill='x', padx=20, pady=(10, 20))

        tk.Button(
            quick_add_frame,
            text="+ Швидко додати завдання",
            bg=COLORS['accent'],
            fg=COLORS['dark'],
            font=FONTS['subtitle'],
            padx=20,
            pady=5,
            command=self.add_quick_task
        ).pack(side='left')

    def add_quick_task(self):
        # Діалогове вікно для швидкого додавання завдання
        dialog = tk.Toplevel(self.root)
        dialog.title("Додати завдання")
        dialog.geometry("400x300")
        dialog.resizable(False, False)

        tk.Label(dialog, text="Предмет:", font=FONTS['regular']).grid(row=0, column=0, padx=10, pady=5, sticky='e')
        subject_var = tk.StringVar()
        subject_dropdown = ttk.Combobox(dialog, textvariable=subject_var, values=self.subjects, state='readonly')
        subject_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        tk.Label(dialog, text="Завдання:", font=FONTS['regular']).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        task_entry = tk.Entry(dialog, font=FONTS['regular'])
        task_entry.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        tk.Label(dialog, text="Термін:", font=FONTS['regular']).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        due_entry = tk.Entry(dialog, font=FONTS['regular'])
        due_entry.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        tk.Button(
            dialog,
            text="Додати",
            bg=COLORS['accent'],
            fg=COLORS['dark'],
            command=lambda: self.save_task(subject_var.get(), task_entry.get(), due_entry.get(), dialog)
        ).grid(row=3, column=1, padx=10, pady=10, sticky='e')

    def save_task(self, subject, task, due, dialog):
        if subject and task and due:
            self.tasks.append({
                "subject": subject,
                "task": task,
                "due": due,
                "status": "Активне",
                "priority": "Середній"
            })
            messagebox.showinfo("Успіх", "Завдання успішно додано!")
            dialog.destroy()
            self.show_home_page()
        else:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля")

    def show_schedule(self):
        self.clear_main_frame()

        # Календар на місяць
        self.calendar_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        self.calendar_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Заголовок календаря
        now = datetime.now()
        self.month_year_label = tk.Label(
            self.calendar_frame,
            text=f"{calendar.month_name[now.month]} {now.year}",
            font=FONTS['subtitle'],
            bg=COLORS['background'],
            fg=COLORS['dark']
        )
        self.month_year_label.pack(pady=(0, 10))

        # Створення календаря
        self.create_calendar_widget(now)

        # Розклад на день
        self.daily_schedule_frame = tk.LabelFrame(
            self.main_frame,
            text="Розклад на сьогодні",
            font=FONTS['subtitle'],
            bg=COLORS['background'],
            fg=COLORS['dark']
        )
        self.daily_schedule_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Таблиця розкладу
        self.schedule_tree = ttk.Treeview(
            self.daily_schedule_frame,
            columns=('time', 'subject', 'room', 'teacher'),
            show='headings',
            height=5
        )

        self.schedule_tree.heading('time', text='Час')
        self.schedule_tree.heading('subject', text='Предмет')
        self.schedule_tree.heading('room', text='Аудиторія')
        self.schedule_tree.heading('teacher', text='Викладач')

        self.schedule_tree.column('time', width=80, anchor='center')
        self.schedule_tree.column('subject', width=150, anchor='w')
        self.schedule_tree.column('room', width=80, anchor='center')
        self.schedule_tree.column('teacher', width=150, anchor='w')

        self.schedule_tree.pack(fill='both', expand=True, padx=5, pady=5)

        # Додати приклад розкладу
        schedule_data = [
            ("08:00-09:30", "Математика", "304", "Іванова І.І."),
            ("10:00-11:30", "Фізика", "205", "Петров П.П."),
            ("12:00-13:30", "Англійська", "101", "Сидорова С.С.")
        ]

        for item in schedule_data:
            self.schedule_tree.insert('', 'end', values=item)

        # Додати кнопки керування
        self.schedule_buttons_frame = tk.Frame(self.daily_schedule_frame, bg=COLORS['background'])
        self.schedule_buttons_frame.pack(fill='x', pady=(0, 5))

        tk.Button(
            self.schedule_buttons_frame,
            text="Додати заняття",
            bg=COLORS['accent'],
            fg=COLORS['dark'],
            command=self.add_schedule_item
        ).pack(side='left', padx=5)

    def create_calendar_widget(self, date):
        # Створення календаря
        self.calendar_canvas = tk.Canvas(
            self.calendar_frame,
            bg=COLORS['light'],
            highlightthickness=0
        )
        self.calendar_canvas.pack(fill='both', expand=True)

        # Дні тижня
        days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]
        day_width = 100
        x_offset = 10

        for i, day in enumerate(days):
            self.calendar_canvas.create_text(
                x_offset + i * day_width + day_width // 2,
                20,
                text=day,
                font=FONTS['subtitle'],
                fill=COLORS['dark']
            )

        # Визначити перший день місяця та кількість днів
        first_day = date.replace(day=1)
        weekday = first_day.weekday()  # 0 - понеділок, 6 - неділя
        num_days = calendar.monthrange(date.year, date.month)[1]

        # Відобразити дні місяця
        day_height = 60
        current_day = 1

        for week in range(6):
            for day in range(7):
                if (week == 0 and day < weekday) or current_day > num_days:
                    continue

                x = x_offset + day * day_width + day_width // 2
                y = 50 + week * day_height + day_height // 2

                # Прямокутник для дня
                self.calendar_canvas.create_rectangle(
                    x_offset + day * day_width + 5,
                    40 + week * day_height + 5,
                    x_offset + (day + 1) * day_width - 5,
                    40 + (week + 1) * day_height - 5,
                    fill=COLORS['light'],
                    outline=COLORS['secondary']
                )

                # Номер дня
                self.calendar_canvas.create_text(
                    x_offset + day * day_width + 15,
                    40 + week * day_height + 15,
                    text=str(current_day),
                    font=FONTS['subtitle'],
                    fill=COLORS['dark'],
                    anchor='nw'
                )

                # Випадкові заняття (приклад)
                if random.random() > 0.7 and current_day <= num_days:
                    subject = random.choice(self.subjects)
                    self.calendar_canvas.create_text(
                        x,
                        y,
                        text=subject[:10],
                        font=FONTS['small'],
                        fill=COLORS['primary'],
                        width=day_width - 10
                    )

                current_day += 1

    def show_tasks(self):
        self.clear_main_frame()

        # Заголовок
        tk.Label(
            self.main_frame,
            text="Мої завдання",
            font=FONTS['subtitle'],
            bg=COLORS['background'],
            fg=COLORS['dark']
        ).pack(pady=(10, 5))

        # Фільтри
        self.filter_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        self.filter_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(
            self.filter_frame,
            text="Фільтрувати:",
            font=FONTS['regular'],
            bg=COLORS['background'],
            fg=COLORS['dark']
        ).pack(side='left')

        self.subject_filter = ttk.Combobox(
            self.filter_frame,
            values=["Усі предмети"] + self.subjects,
            state='readonly',
            width=15
        )
        self.subject_filter.current(0)
        self.subject_filter.pack(side='left', padx=5)

        self.status_filter = ttk.Combobox(
            self.filter_frame,
            values=["Усі статуси", "Активні", "Виконані", "Протерміновані"],
            state='readonly',
            width=15
        )
        self.status_filter.current(0)
        self.status_filter.pack(side='left', padx=5)

        # Таблиця завдань
        self.tasks_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        self.tasks_frame.pack(fill='both', expand=True, padx=10, pady=5)

        self.tasks_tree = ttk.Treeview(
            self.tasks_frame,
            columns=('subject', 'task', 'due_date', 'status', 'priority'),
            show='headings',
            height=10
        )

        self.tasks_tree.heading('subject', text='Предмет')
        self.tasks_tree.heading('task', text='Завдання')
        self.tasks_tree.heading('due_date', text='Термін')
        self.tasks_tree.heading('status', text='Статус')
        self.tasks_tree.heading('priority', text='Пріоритет')

        self.tasks_tree.column('subject', width=120, anchor='w')
        self.tasks_tree.column('task', width=200, anchor='w')
        self.tasks_tree.column('due_date', width=100, anchor='center')
        self.tasks_tree.column('status', width=100, anchor='center')
        self.tasks_tree.column('priority', width=80, anchor='center')

        self.tasks_tree.pack(fill='both', expand=True)

        # Додати приклад завдань
        for task in self.tasks:
            self.tasks_tree.insert('', 'end', values=(
                task['subject'],
                task['task'],
                task['due'],
                task['status'],
                task['priority']
            ))

        # Кнопки керування
        self.task_buttons_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        self.task_buttons_frame.pack(fill='x', padx=10, pady=(0, 10))

        tk.Button(
            self.task_buttons_frame,
            text="Додати завдання",
            bg=COLORS['accent'],
            fg=COLORS['dark'],
            command=self.add_task
        ).pack(side='left', padx=5)

        tk.Button(
            self.task_buttons_frame,
            text="Позначити як виконане",
            bg=COLORS['success'],
            fg=COLORS['light']
        ).pack(side='left', padx=5)

    def show_grades(self):
        self.clear_main_frame()

        # Заголовок
        tk.Label(
            self.main_frame,
            text="Мої оцінки",
            font=FONTS['subtitle'],
            bg=COLORS['background'],
            fg=COLORS['dark']
        ).pack(pady=(10, 5))

        # Вибір предмету
        self.subject_grade_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        self.subject_grade_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(
            self.subject_grade_frame,
            text="Предмет:",
            font=FONTS['regular'],
            bg=COLORS['background'],
            fg=COLORS['dark']
        ).pack(side='left')

        self.grade_subject = ttk.Combobox(
            self.subject_grade_frame,
            values=self.subjects,
            state='readonly',
            width=20
        )
        self.grade_subject.current(0)
        self.grade_subject.pack(side='left', padx=5)

        # Графік оцінок
        self.grades_chart_frame = tk.Frame(self.main_frame, bg=COLORS['light'])
        self.grades_chart_frame.pack(fill='both', expand=True, padx=10, pady=5)

        # Приклад графіку
        self.grades_canvas = tk.Canvas(
            self.grades_chart_frame,
            bg=COLORS['light'],
            highlightthickness=0
        )
        self.grades_canvas.pack(fill='both', expand=True)

        # Намалювати простий графік
        self.draw_sample_chart()

        # Таблиця оцінок
        self.grades_table_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        self.grades_table_frame.pack(fill='both', expand=True, padx=10, pady=5)

        self.grades_tree = ttk.Treeview(
            self.grades_table_frame,
            columns=('date', 'type', 'grade', 'comment'),
            show='headings',
            height=5
        )

        self.grades_tree.heading('date', text='Дата')
        self.grades_tree.heading('type', text='Тип роботи')
        self.grades_tree.heading('grade', text='Оцінка')
        self.grades_tree.heading('comment', text='Коментар')

        self.grades_tree.column('date', width=100, anchor='center')
        self.grades_tree.column('type', width=150, anchor='w')
        self.grades_tree.column('grade', width=80, anchor='center')
        self.grades_tree.column('comment', width=200, anchor='w')

        self.grades_tree.pack(fill='both', expand=True)

        # Додати приклад оцінок
        for grade in self.grades:
            self.grades_tree.insert('', 'end', values=(
                grade['date'],
                grade['type'],
                grade['grade'],
                grade['comment']
            ))

        # Кнопки керування
        self.grade_buttons_frame = tk.Frame(self.main_frame, bg=COLORS['background'])
        self.grade_buttons_frame.pack(fill='x', padx=10, pady=(0, 10))

        tk.Button(
            self.grade_buttons_frame,
            text="Додати оцінку",
            bg=COLORS['accent'],
            fg=COLORS['dark'],
            command=self.add_grade
        ).pack(side='left', padx=5)

    def draw_sample_chart(self):
        # Простий приклад графіку
        width = self.grades_chart_frame.winfo_width() or 400
        height = 200
        padding = 40

        # Ось X
        self.grades_canvas.create_line(padding, height - padding, width - padding, height - padding, width=2)
        # Ось Y
        self.grades_canvas.create_line(padding, padding, padding, height - padding, width=2)

        # Позначки на осях
        for i in range(1, 6):
            y = height - padding - i * 30
            self.grades_canvas.create_line(padding - 5, y, padding + 5, y, width=1)
            self.grades_canvas.create_text(padding - 20, y, text=str(i * 2), font=FONTS['small'])

        # Підписи
        self.grades_canvas.create_text(width // 2, height - 10, text="Тижні", font=FONTS['small'])
        self.grades_canvas.create_text(15, height // 2, text="Оцінки", font=FONTS['small'], angle=90)

        # Дані (приклад)
        data = [4, 7, 6, 9, 8, 10]
        for i in range(len(data)):
            x = padding + (i + 1) * 50
            y = height - padding - data[i] * 15
            self.grades_canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=COLORS['primary'])
            if i > 0:
                prev_x = padding + i * 50
                prev_y = height - padding - data[i - 1] * 15
                self.grades_canvas.create_line(prev_x, prev_y, x, y, fill=COLORS['primary'], width=2)

    def add_schedule_item(self):
        # Діалогове вікно для додавання заняття
        dialog = tk.Toplevel(self.root)
        dialog.title("Додати заняття")
        dialog.geometry("400x300")
        dialog.resizable(False, False)

        tk.Label(dialog, text="Предмет:", font=FONTS['regular']).grid(row=0, column=0, padx=10, pady=5, sticky='e')
        subject_var = tk.StringVar()
        subject_dropdown = ttk.Combobox(dialog, textvariable=subject_var, values=self.subjects, state='readonly')
        subject_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        tk.Label(dialog, text="Час:", font=FONTS['regular']).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        time_entry = tk.Entry(dialog, font=FONTS['regular'])
        time_entry.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        tk.Label(dialog, text="Аудиторія:", font=FONTS['regular']).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        room_entry = tk.Entry(dialog, font=FONTS['regular'])
        room_entry.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        tk.Button(
            dialog,
            text="Додати",
            bg=COLORS['accent'],
            fg=COLORS['dark'],
            command=lambda: self.save_schedule(subject_var.get(), time_entry.get(), room_entry.get(), dialog)
        ).grid(row=3, column=1, padx=10, pady=10, sticky='e')

    def save_schedule(self, subject, time, room, dialog):
        if subject and time and room:
            # Тут буде логіка збереження розкладу
            messagebox.showinfo("Успіх", "Заняття успішно додано!")
            dialog.destroy()
        else:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля")

    def add_task(self):
        # Діалогове вікно для додавання завдання
        dialog = tk.Toplevel(self.root)
        dialog.title("Додати завдання")
        dialog.geometry("400x300")
        dialog.resizable(False, False)

        tk.Label(dialog, text="Предмет:", font=FONTS['regular']).grid(row=0, column=0, padx=10, pady=5, sticky='e')
        subject_var = tk.StringVar()
        subject_dropdown = ttk.Combobox(dialog, textvariable=subject_var, values=self.subjects, state='readonly')
        subject_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        tk.Label(dialog, text="Завдання:", font=FONTS['regular']).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        task_entry = tk.Entry(dialog, font=FONTS['regular'])
        task_entry.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        tk.Label(dialog, text="Термін:", font=FONTS['regular']).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        due_entry = tk.Entry(dialog, font=FONTS['regular'])
        due_entry.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        tk.Button(
            dialog,
            text="Додати",
            bg=COLORS['accent'],
            fg=COLORS['dark'],
            command=lambda: self.save_task(subject_var.get(), task_entry.get(), due_entry.get(), dialog)
        ).grid(row=3, column=1, padx=10, pady=10, sticky='e')

    def add_grade(self):
        # Діалогове вікно для додавання оцінки
        dialog = tk.Toplevel(self.root)
        dialog.title("Додати оцінку")
        dialog.geometry("400x300")
        dialog.resizable(False, False)

        tk.Label(dialog, text="Предмет:", font=FONTS['regular']).grid(row=0, column=0, padx=10, pady=5, sticky='e')
        subject_var = tk.StringVar()
        subject_dropdown = ttk.Combobox(dialog, textvariable=subject_var, values=self.subjects, state='readonly')
        subject_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        tk.Label(dialog, text="Тип роботи:", font=FONTS['regular']).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        type_var = tk.StringVar()
        type_dropdown = ttk.Combobox(dialog, textvariable=type_var,
                                     values=["Контрольна", "Лабораторна", "Тест", "Домашня"], state='readonly')
        type_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky='we')

        tk.Label(dialog, text="Оцінка:", font=FONTS['regular']).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        grade_entry = tk.Entry(dialog, font=FONTS['regular'])
        grade_entry.grid(row=2, column=1, padx=10, pady=5, sticky='we')

        tk.Button(
            dialog,
            text="Додати",
            bg=COLORS['accent'],
            fg=COLORS['dark'],
            command=lambda: self.save_grade(subject_var.get(), type_var.get(), grade_entry.get(), dialog)
        ).grid(row=3, column=1, padx=10, pady=10, sticky='e')

    def save_grade(self, subject, type_, grade, dialog):
        if subject and type_ and grade:
            # Тут буде логіка збереження оцінки
            messagebox.showinfo("Успіх", "Оцінку успішно додано!")
            dialog.destroy()
        else:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля")

    def show_stats(self):
        self.clear_main_frame()
        tk.Label(
            self.main_frame,
            text="Статистика успішності",
            font=FONTS['subtitle'],
            bg=COLORS['background'],
            fg=COLORS['dark']
        ).pack(pady=10)

        # Приклад статистики
        stats_frame = tk.Frame(self.main_frame, bg=COLORS['light'], padx=10, pady=10)
        stats_frame.pack(fill='both', expand=True, padx=20, pady=10)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudyBuddyApp(root)
    root.mainloop()