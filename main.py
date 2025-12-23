# data/2025/Q4
import os

# крок 1: ввести шлях до кварталу
quarter_path = input("Enter path to quarter folder: ")

# перевірка існування каталогу
if not os.path.isdir(quarter_path):
    print(f"ERROR: Quarter directory not found: {quarter_path}")
    exit(1)

print(f"Quarter directory found: {quarter_path}")

# крок 2: визначити джерела (sources)
sources = [name for name in os.listdir(quarter_path)
           if os.path.isdir(os.path.join(quarter_path, name))]
print(f"Sources found: {sources}\n")

# крок 3: обробка кожного source
for source in sources:
    print(f"Processing source: {source}")
    source_path = os.path.join(quarter_path, source)

    # для PayPal потрібно заходити в підпапки місяця
    if source.lower() == 'paypal':
        months = [name for name in os.listdir(source_path)
                  if os.path.isdir(os.path.join(source_path, name))]
        print(f"Months found for paypal: {months}")

        for month in months:
            month_path = os.path.join(source_path, month)
            csv_files = []
            # рекурсивний пошук у всіх підпапках місяця
            for root, dirs, files in os.walk(month_path):
                for file in files:
                    if file.endswith('.csv'):
                        csv_files.append(os.path.join(root, file))
            if not csv_files:
                print(f"WARNING: No CSV files found in {month_path}")
            else:
                print(f"CSV files in {month}/{source}: {csv_files}")

    # для Stripe файли лежать без підпапок
    else:
        months = [name for name in os.listdir(source_path)
                  if os.path.isdir(os.path.join(source_path, name))]
        print(f"Months found for {source}: {months}")

        for month in months:
            month_path = os.path.join(source_path, month)
            csv_files = [os.path.join(month_path, f)
                         for f in os.listdir(month_path)
                         if f.endswith('.csv')]
            if not csv_files:
                print(f"WARNING: No CSV files found in {month_path}")
            else:
                print(f"CSV files in {month}/{source}: {csv_files}")
