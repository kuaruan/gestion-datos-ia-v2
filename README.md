Máquina de gestión independiente

1. Portabilidad Total (Docker)

 Dockerfile y requirements.txt  aplicación = paquete sellado.

Lleva su propio "sistema operativo" y librerías dentro.

2. Calidad Garantizada (GitHub Actions)

 main.yml es el Control de Calidad (CI).

Si el código tiene un error que impide que Docker se construya, el pipeline fallará y avisará antes de que el error llegue a los usuarios.

3. Entrega Continua (Render)

El objetivo de conectar GitHub con Render es el Despliegue Continuo (CD).

 En cuanto exista un git push, el servidor se actualizará 
