import shutil, time, os
clear = lambda: os.system('cls')
pause = lambda: os.system('pause')


clear()
diretorio_atual = input('COLOQUE O LINK DA PASTA PARA SER ORGANIZADA: ')
print('')


EXTENCOES_DICIONARIO = {
    'IMAGENS':      ['.jpg','.png','.gif','.ico','.psd','.webp','.raw','.jpeg','.lif','.bmp','.tif','.svg','.ai','.JPG','.PNG','.GIF','.ICO','.PSD','.WEBP','.RAW','.JPEG','.LIF','.BMP','.TIF','.SVG','.AI'],
    'VIDEOS':       ['.mp4','.mkv','.avi','.3gp','.webm','.mpeg','.wmv','.mov','.flv','.MP4','.MKV','.AVI','.3GP','.WEBM','.MPEG','.WMV','.MOV','.FLV'],
    'AUDIO':        ['.mp3','.flac','.m4a','.wav','.aac','.MP3','.FLAC','.M4A','.WAV','.AAC'],
    'OFFICE_EXCEL': ['.xls','.xlsx','.xlsm','.xlsb','.xltx','.xltm','.xla','.xlam','.XLS','.XLSX','.XLSM','.XLSB','.XLTX','.XLTM','.XLA','.XLAM'],
    'OFFICE_WORD':  ['.doc','.docx','.docm','.dotx','.dot','.dotm','.pdf','.DOC','.DOCX','.DOCM','.DOTX','.DOT','.DOTM','.PDF'],
    'OFFICE_POWER': ['.pptx','.pptm','.ppt','.potx','.potm','.pot','.thmx','.ppsx','.ppsm','.pps','.odp','.PPTX','.PPTM','.PPT','.POTX','.POTM','.POT','.THMX','.PPSX','.PPSM','.PPS','.ODP'],
    'COMPRESSED':   ['.iso','.zip','.rar','.7z','.tgz','.tar','.bz','.ISO','.ZIP','.RAR','.7Z','.TGZ','.TAR','.BZ'],
    'DEVELOPMENT':  ['.py','.c','.cpp','.dart','.js','.bat','.sh','.PY','.C','.CPP','.DART','.JS','.BAT','.SH'],
    'PROGRAMAS':    ['.exe','.msi','.EXE','.MSI'],
    'OUTROS':       ['.csv','.CSV','.sql','.SQL']}

def CRIAR_DIRETORIOS(nome_pasta):
    try:
        if nome_pasta == "":
            print('>>> NÃO É POSSIVEL CRIAR PASTAS SEM NOME <<<')
        else:
            os.makedirs(f'{diretorio_atual}\{nome_pasta}') #exist_ok = true
            print(f'>>> DIRETORIO CRIADO COM SUCESSO >>> "{nome_pasta}"')
    

    except(OSError, FileExistsError):
        if os.path.isdir(diretorio_atual):
            print(f'>>> O DIRETORIO JÁ EXISTE: "{diretorio_atual}\{nome_pasta}"')
        else:
            print(f'>>> NÃO FOI POSSIVEL CRIAR O DIRETORIO >>> "{nome_pasta}"')
        pass

    finally:
        #if os.path.isdir(diretorio_atual):
        #    print(f'>>> O DIRETORIO JÁ EXISTE: "{diretorio_atual}\{nome_pasta}"')
        pass

def REMOVER_DIRETORIO_VAZIO(diretorio):
    PASTAS_LISTA = []
    for diretorios in os.listdir(diretorio):
        PASTAS_LISTA.append(diretorios)

    for i in range(0, len(PASTAS_LISTA)):
        try:
            os.rmdir(f'{diretorio}\{PASTAS_LISTA[i]}')
        except:
            print(f'A PASTA NÃO ESTA VAZIA, OU NÃO PODE SER MODIFICADA: {diretorio}\{PASTAS_LISTA[i]}')
            i+1

def ORGANIZA_PASTA(lista_extensoes, nome_pasta):
    for dados in os.listdir(diretorio_atual):
        filename, file_ext = os.path.splitext(dados) 
        try:
            if not file_ext:
                pass
            elif file_ext in lista_extensoes:
                shutil.move(
                    os.path.join(diretorio_atual, f'{filename}{file_ext}'),
                    os.path.join(diretorio_atual, nome_pasta, f'{filename}{file_ext}'))
        finally:
            pass

def PRINT_LAYER():
    print('=========================================================================================================')

def MODULES_INSTALL():
    try:
        os.system('pip install shutil')
    except:
        pass

def EXEC_PROGRAMA():
    #MODULES_INSTALL()
    PRINT_LAYER()

    for i in EXTENCOES_DICIONARIO:
        CRIAR_DIRETORIOS(i)
        ORGANIZA_PASTA(EXTENCOES_DICIONARIO[i],i)

    PRINT_LAYER()
    time.sleep(1)

    REMOVER_DIRETORIO_VAZIO(diretorio_atual)
    PRINT_LAYER()



EXEC_PROGRAMA()
pause()




