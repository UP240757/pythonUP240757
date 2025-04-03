print("Ejercicio 5.1:")
import countries_data as cd

def most_spoken_languages(data, n=10):
    languages_count = {}
    for country in data:
        for language in country['languages']:
            languages_count[language] = languages_count.get(language, 0) + 1
    sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

# Example usage:
top_languages = most_spoken_languages(cd.countries, 10)
print("Los 10 idiomas más hablados en el mundo son:")
for language, count in top_languages:
    print(f"{language}: {count} países")



        












