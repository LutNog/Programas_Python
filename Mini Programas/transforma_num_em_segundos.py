total_segs = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = total_segs // 86400
horas_restantes = total_segs % 86400
horas = horas_restantes // 3600
segs_restantes = horas_restantes % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias," , horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")