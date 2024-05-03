import phonenumbers
from geopy.geocoders import GoogleV3

def rastrear_numero(numero):
    # Converte o número para o formato internacional
    numero_internacional = phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.E164)

    # Obtém a localização do número
    try:
        loc = phonenumbers.parse(numero_internacional, None)
        geolocalizacao = GoogleV3().geocode(loc.country_code + loc.national_number)
        return {
            "localizacao": geolocalizacao.address,
            "operadora": phonenumbers.carrier(loc),
        }
    except phonenumbers.NumberParseException:
        return None


print(rastrear_numero("+5521999999999"))
