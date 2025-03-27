import wikipediaapi

def main():
    wiki = wikipediaapi.Wikipedia(user_agent='MyProjectName (merlin@example.com)', language='en')
    
    # Generate pages to scrape (1990-2021)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December']
    
    years = list(range(1990, 1992))  # 1990 to 2021 inclusive
    
    # Build and process all pages
    all_deaths = {}
    
    for year in years:
        all_deaths[year] = {}
        for month in months:
            page_name = f'Deaths_in_{month}_{year}'
            page = wiki.page(page_name)
            
            if page.exists():
                print(f"Processing {month} {year}...")
                all_deaths[year][month] = parse_page(page.text, month, year)
            else:
                print(f"Page {page_name} does not exist, skipping.")
    
    # Now you have a nested dictionary: all_deaths[year][month][day] = list of death entries
    
    # Example: Print deaths from January 1, 1990
    if 1990 in all_deaths and 'January' in all_deaths[1990] and 1 in all_deaths[1990]['January']:
        print("Deaths on January 1, 1990:")
        for entry in all_deaths[1990]['January'][1]:
            print(f"- {entry}")

def parse_page(text, month, year):
    day_text = {}
    current_day = None
    
    text_divided = text.split("\n")
    
    for line in text_divided:
        # Try to parse the line as a day number
        if line.strip().isdigit() and 1 <= int(line) <= 31:
            current_day = int(line)
            day_text[current_day] = []
        # If we have a current day and the line isn't empty, add it to that day's entries
        elif line.strip() and current_day is not None:
            day_text[current_day].append(line)
    
    print(day_text)
    return day_text

if __name__ == "__main__":
    main()