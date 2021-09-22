import psutil
from funcoes import formata_tamanho

def q1():
    
    processos = {}

    processos_ativos = psutil.pids()
    nomes_processos = []
    for proc in processos_ativos:
        try:
            processo = psutil.Process(proc)
            nome_processo = processo.name()

            if nome_processo not in nomes_processos:
                processos[proc] = {}
                processos[proc]["pid"] = processo.pid
                processos[proc]["nome"] = nome_processo
                processos[proc]["status"] = processo.status()
                processos[proc]["memoria"] = processo.memory_info()[1]
                processos[proc]["memoria_uso"] = processo.memory_percent()
                processos[proc]["threads"] = processo.num_threads()
                processos[proc]["cpu_percent"] = processo.cpu_percent(interval=1) / psutil.cpu_count()

                nomes_processos.append(nome_processo)
            else:
                processos[proc]["memoria"] += processo.memory_info()[1]
                processos[proc]["memoria_uso"] += processo.memory_percent()
                processos[proc]["threads"] += processo.num_threads()
                processos[proc]["cpu_percent"] += processo.cpu_percent()

        except psutil.NoSuchProcess as e:
            msg = f"Processo de PID {proc} não está em execução"
            print(msg)
            processos[proc] = {}
            processos[proc]["pid"] = proc
            processos[proc]["status"] = msg
            processos[proc]["memoria"] = 0

        except Exception:
            pass

    processos = [i[1] for i in sorted(processos.items(), key=lambda x: x[1]['memoria'], reverse=True)] #ordenando por memoria
    
    processos_retorno = {}
    for p in processos:
        index = processos.index(p)
        processos_retorno[index] = p
        processos_retorno[index]["memoria"] = formata_tamanho(p["memoria"])
        try:
            processos_retorno[index]["memoria_uso"] = round(p["memoria_uso"],2)
            processos_retorno[index]["cpu_percent"] = round(p["cpu_percent"], 2)
        except:
            pass
    return processos_retorno

q1_processos = q1()

for p in q1_processos:
    print(q1_processos[p])