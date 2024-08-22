from bs4 import BeautifulSoup
import pandas as pd
from contextlib import suppress


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_table_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table', class_='fipeTableModels')
    data = []

    if not tables:
        print('Nenhuma tabela com a classe fipeTableModels encontrada no HTML.')
        return data

    for table in tables:
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 2:
                codigo_fipe = cols[0].text.strip()
                modelo = cols[1].text.strip()
                data.append({'Código FIPE': codigo_fipe, 'Modelo': modelo})

    return data


def save_to_csv(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding='utf-8')
    print(f'Dados salvos no arquivo {file_path}')

def main():
    html_file_path = 'index.html'
    csv_file_path = 'modelos_fipe.csv'

    html_content = read_html_file(html_file_path)
    data = extract_table_data(html_content)

    if data:
        save_to_csv(data, csv_file_path)

if __name__ == "__main__":
    main()
