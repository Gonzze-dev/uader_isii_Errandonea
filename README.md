# Ingenieria de software II
## Primer Taller
### PROFES
 - Julian Escalante
 - Pablo Collar

Mi pagina web [![YardSale](https://gonzze-dev.github.io/Yard-Sale/assets/logos/logo_yard_sale.svg)](https://gonzze-dev.github.io/Yard-Sale/)
> se hosteo en git porque no pienso pagar un host.

## Pasos que se hicieron para la resolucion del tp
###### paso 1
1. se creo un repositorio en git yendo a "repositorios -> new" alli puse UADER_ISII_Errandonea de nombre del repo y lo cree.

###### paso 2
1. cree las carpetas
  - python
  - docs
  - bash
  - bin 
  - images 
en una carpeta que tengo exclusiva para la materia.

###### paso 3
1. Se decargue el archivo del aula virtual del muddle *primos.py* de la carpeta *trabajos practicos -> Gestión de la Configuración - Uso de Git y GitHub -> Apéndice*.
2. Coloque el archivo en la carpeta *python*.

###### paso 4
1. testee el archivo py por el bash de git, simplemente colocandome en la carpeta donde tenia creda las anteriores carpetas, alli abri el bash de git, *click derecho y abri el bash ahi*, luego, escribir ```cd ./python``` para colocarme en la carpeta y luego puse ```py primos.py``` y luego lo empece a probar.
> eso de poner cd, y demas fue para probar el bash de git, para adaptarme a el.

###### paso 5
1. una vez probe el archivo, en la misma carpeta, donde estaban creadas las carpetas de python, y de mas, con el bash abierto, puse los siguientes comandos.

```
git init "UADER_ISII_Errandonea"
git config --global user.email "errandoneagonzalo18@gmail.com"
git config --global user.name "Gonzze"
git add *
git commit -M "Primer Commit"
git remote add origin https://github.com/Gonzze-dev/uader_isii_Errandonea.git
git push -u origin main
```
2. Luego de eso, me pidio iniciar sesion, una vez inicie, se subio todo.

###### paso 6
1. borre el archivo *primos.py* de la carpeta *python*.
2. abri el bash en la anterior carpeta a la de *python*.
3. alli puse ```git status``` para ver si el archivo estaba borrado.
4. el mismo git me decia que el archivo habia sido borrado, pero que lo podia recuperar con ```git restore + carpeta/archivo.extencion```.
5. por ultimo, puse ```git restore python/primos.py``` para recuperarlo.

###### paso 7
