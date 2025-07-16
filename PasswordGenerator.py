options = {
    'upper': False,
    'lower': False,
    'digit': False,
    'symbol': False,
}

def config_senha(options):
    while True:
        try:
            num_carac = int(input('\nDigite quantos caracteres terá sua senha. (8 - 20)'))
            if not 8 <= num_carac <= 20:
                print('Valor invalido. O numero de caracteres deve estar entre 8 e 20')
                continue
            else:
                break
        except ValueError:
            print("\nValor Invalido. Por favor, digite um VALOR NUMERICO.\n")
            continue
    
    while True:
        print('Selecione uma opcao para swita-la')
        print('*'*40)
        print('  Configurações da Senha:')

        option_list = list(options.keys())
        for idx, key in enumerate(option_list):
            status = '✔' if options[key] else '❌'
            print(f'    ({idx+1}) {key.ljust(7)}: {status}')

        print(f'\n  ({len(options) + 1}) Finalizar Configurações!')
        print('*'*40)
        
        try:
            opt = int(input()) - 1
            if not 0 <= opt <= len(options):
                print(f'\nValor Invalido. Digite um valor entre 1 e {len(options) + 1}\n')
                continue
        except ValueError:
            print("\nValor Invalido. Por favor, digite um VALOR NUMERICO.\n")
            continue

        if opt == len(options):
            if not any(options.values()):
                print('É impossivel criar uma senha sem caracteres. Por favor ative, ao menos, uma opção.')
                continue
            return options, num_carac
        options[option_list[opt]] = not options[option_list[opt]]
        

def generator(options):
    import random
    import string

    options, num_carac = config_senha(options)
    active_opt = {k: v for k, v in options.items() if v}
    tipos_ativos = list(active_opt)
    char_set = {
        'upper': string.ascii_uppercase,
        'lower': string.ascii_lowercase,
        'digit': string.digits,
        'symbol': string.punctuation + ' '
        }

    senha = []
    
    for tipo in active_opt:
        char = random.choice(char_set[tipo])
        senha.append(char)
        print(senha, len(senha))
    
    while len(senha) < num_carac:
        tipo_aleatorio = random.choice(tipos_ativos)
        print(tipo_aleatorio)
        char = random.choice(char_set[tipo_aleatorio])

        senha.append(char)
        print(senha, len(senha))

    random.shuffle(senha)    
    senha_final = ''.join(senha)
    print(senha_final, len(senha_final))

generator(options)