from gtts import gTTS
import os

# Your Spanish script
spanish_script = """


Bienvenido a TruckMetrics video

Esta es una sesión de capacitación del MetricsManager Pro, diseñada para brindarte instrucciones claras.
Específicamente, para usuarios de MetricsManager Pro que han instalado TruckMetrics en sus sitios.  

Ten en cuenta que esta capacitación no incluye hardware ni información de instalación, para eso, 
consulta el manual de TruckMetrics, que puedes encontrar adjunto en este artículo.  

La agenda de hoy abarca los módulos disponibles en TruckMetrics, 
incluyendo las características en MetricsManager Pro, como el tablero, distribución de tamaño de partícula, PSD, productividad y reportabilidad de la galería.  

Comenzaremos revisando todos los módulos disponibles para TruckMetrics.  

TruckMetrics es una solución integral para monitoreo de cargas en camiones de transporte, que ofrece detección avanzada, análisis de tamaño de partícula, perfil de carga y volumen, todo sin interrumpir la producción.  

Cuenta con un sistema automatizado de limpieza de lentes y utiliza inteligencia artificial y 
una cámara estéreo 3D montada en un pórtico para ofrecer análisis en tiempo real.  

Además, está conectado a la plataforma en línea MetricsManager Pro, 
permitiendo acceso a análisis e informes desde cualquier lugar.  

Los módulos en MetricsManager Pro incluyen detección de bolones, 
ayudando a reducir el tiempo de inactividad y el uso de interruptores de roca.
También ayuda a prevenir desgaste desigual de camiones mediante perfiles de carga precisos, 
y realiza análisis de tamaño de partícula y evaluación de la explosión, analizando la distribución en cada carga.  

Para detectar y optimizar la producción, mide el volumen de cada carga de camiones.  

Si deseas más información, contacta a un representante de Weir Motion Metrics o a nuestro equipo de soporte.  

Las características disponibles en MetricsManager Pro incluyen el panel de control, tamaño de partícula y galería de productividad.  

MetricsManager Pro es una plataforma en línea que centraliza todos los datos del usuario en un solo lugar.
Con su interfaz intuitiva y actualizaciones en tiempo real, te permite recibir notificaciones críticas y generar informes fácilmente.  

Puedes acceder a MetricsManager Pro desde computadoras, tablets o teléfonos móviles, asegurando que toda la información esté disponible en cualquier lugar.  

Recuerda que los usuarios solo tendrán acceso a las cuentas vinculadas a su sitio específico.  

En el tablero, verás la imagen más reciente de cada sistema instalado, con una visión general de los datos de las últimas 12 horas.  

El panel muestra indicadores como el porcentaje de camiones con rocas detectadas, en naranja, y sin rocas, en verde.
Por ejemplo, en las últimas 12 horas, el 97% de los camiones no tenían rocas, mientras que el 3% sí.  

También verás datos sobre el tamaño de partículas, como el porcentaje de material menor a un centímetro, y la tasa de producción en toneladas por hora.  

Si la tasa de producción está en naranja, significa que está por debajo del objetivo.
El panel también muestra el porcentaje de cargas fuera y dentro del objetivo, con opciones para activar o desactivar estas superposiciones en la pantalla.  

Las notificaciones de rocas detectadas aparecerán como ventanas emergentes, y puedes ver todas las notificaciones en el ícono de la campana en la esquina superior.  

Desde allí, puedes confirmar o descartar las alertas.  

Al hacer clic en la imagen de un camión, accederás a una página con detalles de productividad y galería.  

Para navegar la distribución del tamaño de partícula, PSD, debes hacer clic en la imagen del camión en el panel y luego en el icono de PSD.
Desde allí, puedes filtrar datos por rango de tiempo, estado y otros parámetros.  

Por defecto, puedes seleccionar intervalos como las últimas 24 horas, siete días o 31 días, sin exceder ese límite.  

Para filtrar por estado del camión, simplemente selecciona las opciones correspondientes.
El usuario debe hacer clic en el botón de estado del camión y luego seleccionar el camión completo, 
que muestra el número total de camiones identificados por el sistema. En este ejemplo, 
se exhiben un total de 135 camiones debajo del camión completo.  


El sistema proporciona información sobre el estado de las rocas cuando el camión está lleno de material, 
indicando si la roca está confirmada, detectada o no presente.  

Si el camión está vacío, el usuario puede obtener información sobre el estado de la bandeja, incluyendo si se ha confirmado daño en la bandeja,
 o si no hay confirmación de daños en otro camión. Esto también aplica a otros tipos de vehículos.  

El usuario puede filtrar los datos por valores P o especificar un rango de tamaños. Para hacer esto, debe hacer clic en el botón de Valores P, 
seleccionar el valor P deseado en el diálogo que aparece, mover el control deslizante al valor correspondiente y hacer clic en 'Aplicar'.  

El valor P representa el porcentaje de material que es más pequeño que cierto tamaño. Por ejemplo, 
si el valor P 80 corresponde a 10.8 centímetros, significa que el 80% del material en la carga de camiones es menor a esa medida.  

En este ejemplo, el valor P 80 es de 10.8 centímetros, con un mínimo de 11.6 centímetros, un promedio de 13.9 centímetros y un máximo de 16.2 centímetros.  

En la sección de KPI, el usuario puede seleccionar un valor de P diferente si desea revisar otra información.  

Es importante destacar que estos valores de P están disponibles en incrementos de 10, desde 10 hasta 100. 
Además, los valores por debajo de un centímetro representan aproximadamente el 16.9% del total en ese período.  

Junto con esta información, el sistema muestra el número de rocas detectadas en ese período.  

La tasa de producción en volumen total por hora se calcula usando una densidad predeterminada de 1.4 toneladas por metro cúbico. 
Si este valor necesita ser ajustado, el usuario debe ponerse en contacto con el equipo de soporte.  

La barra de posición indica el porcentaje de cargas fuera del objetivo, en naranja, y las cargas dentro del objetivo, en verde.  

También hay una opción para editar los parámetros de KPI. El usuario puede ajustar estos valores según las necesidades específicas de cada mina. 
Para ello, debe hacer clic en 'Editar KPI', realizar los cambios y luego en 'Hecho' para guardar.  

El gráfico de distribución de tamaño de partícula muestra cómo varía el tamaño a lo largo del tiempo. 
Por defecto, presenta la distribución ordenada por el valor P 80.  

Los usuarios pueden seleccionar otro valor de P para mostrar en el gráfico, y los datos se ajustarán en consecuencia. 
Por ejemplo, si seleccionan P 90, los puntos en el gráfico reflejarán esa distribución.  

El gráfico utiliza tres colores: verde para partículas que no contienen rocas, naranja para rocas detectadas pero aún no confirmadas, y rojo para rocas confirmadas.  

Para ver los detalles de un punto de datos en el gráfico, solo debes pasar el cursor sobre él. Si haces clic en un punto, se mostrará la sección de registro correspondiente, permitiéndote alternar la superposición o apagarla.  


Puedes ajustar la opacidad de la superposición arrastrando el control deslizante correspondiente.  

Para navegar entre registros, utiliza las flechas izquierda y derecha. 
La más reciente estará en la parte superior para facilitar la revisión de la distribución del tamaño de partícula y los detalles de PSD.  

Para ver los detalles de la segmentación en un registro específico, simplemente haz clic en la imagen de ese registro en el gráfico.

Aquí podemos ver la imagen del registro seleccionado, junto con el estado del boulder y los KPIs asociados. También se muestra la fecha, 
hora y el valor P80 correspondiente a ese volumen de registro, incluyendo la compensación de tonelaje.

En este ejemplo, el camión está cargado un 6.7% más hacia la derecha. Además, se puede ajustar la opacidad de la superposición para una mejor visualización.

Al hacer clic en un registro dentro de la segmentación, se mostrará la distribución del tamaño de partícula específica para ese registro. 

Esta sección explica cómo funciona la página de análisis de tamaño de partícula para un registro determinado.

Desde esa página, los usuarios pueden ver la imagen del registro, analizar la distribución del tamaño de partícula, 
comparar diferentes valores P y revisar el tamaño objetivo.

Para obtener más detalles del análisis del tamaño de partícula en un registro específico, 
basta con hacer clic sobre la imagen mientras se está en la página TruckMetrics PSD, ubicada al lado derecho.

La tabla de valores P muestra el porcentaje de material que es más pequeño que cierto tamaño.

 En la sección de tamaño objetivo, también se puede ver el porcentaje de material que está dentro del rango deseado, en función de centímetros específicos.

La imagen con superposición muestra las rocas en color amarillo, el material fino en azul y las rocas sobresalientes en rojo.

Si se desea conocer el tamaño de tamiz y la distancia a la cámara de una partícula, solo hay que pasar el cursor sobre una roca en la imagen. 

Automáticamente se mostrará su tamaño lateral y la distancia entre la partícula y la cámara.

En la parte inferior, una barra resalta el estado de la roca, el valor P80, el volumen y la carga útil.

Los usuarios también pueden acceder a funciones adicionales, como cambiar entre vistas de cámara. Para hacerlo, se hace clic en el primer botón de la cámara.

Es posible mostrar u ocultar la superposición y ajustar su opacidad. También hay una vista en 3D, la cual se puede activar haciendo clic en el botón correspondiente.

A través de las cámaras primarias y secundarias, se puede hacer clic y arrastrar para ver el camión desde diferentes ángulos.

La opción de superposición permite encender o apagar la visualización de capas, y con el control deslizante se puede ajustar la opacidad según la preferencia del usuario.

Además, los usuarios ahora pueden comunicarse directamente con los desarrolladores añadiendo preguntas o comentarios desde la misma plataforma.

La imagen también se puede descargar y guardar en la computadora para futuras referencias.

En la esquina superior derecha de la pantalla hay cuatro íconos que ofrecen funciones útiles: dar me gusta o eliminar imágenes similares, reportar resultados que necesitan mejora, 
descargar imágenes o salir de la página actual.

Una vez familiarizados con la distribución del tamaño de partículas, el siguiente paso es navegar por la página de productividad en MetricsManager Pro.

Desde el tablero de TruckMetrics, simplemente se selecciona la unidad deseada para ver más detalles. Luego, se elige la opción de productividad en la parte superior izquierda de la pantalla.

Esta página muestra filtros de datos, KPIs, información sobre el volumen del registro seleccionado, detalles sobre la posición de carga y un gráfico de productividad.

Los filtros en la pestaña de productividad son iguales a los de la pestaña PSD.

La imagen de la posición de carga indica qué tan centradas están las cargas de los camiones al pasar por el pórtico. Cada punto en el gráfico representa una carga, y al seleccionarlo se muestra la imagen correspondiente.

La posición ideal de carga se encuentra dentro de un cuadro verde. Si está fuera de ese rango, el punto se marca en rojo, indicando que está fuera de los límites aceptables.

El gráfico de sesgo delantero y trasero muestra cómo se distribuyen las cargas a lo largo de la bandeja del camión, de 0% a 100%, donde 0% es la parte trasera y 100% la parte delantera.

La alineación ideal de la carga debería estar entre el 50% y el 80%. Si se desvía de este rango, es probable que haya prácticas de carga deficientes.

Finalmente, el sesgo lateral indica cómo se distribuyen las cargas a los lados de la bandeja, desde un 50% negativo (lado izquierdo) hasta un 50% positivo (lado derecho). 

Lo ideal es que la carga esté centrada dentro de un rango de -20% a 20%.

La distribución debe estar contenida dentro de un rango específico. Si se presentan desviaciones fuera de ese rango, probablemente sean señal de malas prácticas de carga.

El gráfico de productividad muestra el volumen del camión. Al hacer clic en una línea, que representa una carga de camión dentro del gráfico, 

se actualiza la imagen del volumen del registro seleccionado, junto con la información de la posición de carga.

Al seleccionar el volumen de un registro específico, se despliega información detallada sobre la productividad de esa carga. 

En esa página, los usuarios pueden ver la imagen de la carga del camión, así como su perfil de material en 2D y la posición de carga.

La superposición del mapa de distancia en la carga del camión resalta en verde las áreas donde hay una mayor concentración de material, y en azul, las zonas con menor presencia.

El perfil de material en 2D incluye un gráfico que muestra el perfil topográfico de la carga. La línea púrpura vertical, ubicada al lado derecho del gráfico, 

se corresponde con una línea horizontal del mismo color en la parte superior de la imagen del camión.

La región verde oscuro representa el volumen máximo alcanzado por el camión, mientras que el verde claro indica el volumen promedio.

Para navegar a la galería de TruckMetrics en MetricsManager Pro, haz clic en una imagen dentro del tablero de TruckMetrics, 
y luego selecciona la opción "Galería" en el menú superior.

La vista de galería organiza los registros por fecha, dentro del rango ya seleccionado por el usuario. Es importante recordar que ese rango no puede superar los 31 días.

Los usuarios pueden filtrar los registros por período, estado, ID del camión y valores P. Cada registro incluye una imagen con la fecha, 
hora e identificación del camión. Un ícono debajo indica si el camión está completo o vacío.

Para ver registros con un estado específico de Boulder, haz clic en la casilla correspondiente dentro de la sección de estado del camión.


 En camiones completos, existen tres estados marcados con colores: rojo para roca confirmada, naranja para Boulder detectada, y verde para ausencia de roca.

En camiones vacíos, también hay tres estados: rojo con círculo lleno para daño confirmado en la bandeja, naranja sin círculo lleno para daño detectado, y verde sin círculo para bandejas sin daño.

Los usuarios pueden generar una vista previa del informe directamente en el navegador y descargar una versión en PDF. Para ello, haz clic en "Crear informe", 

selecciona "Informe web", agrega las fuentes que deseas incluir, edita el título, ajusta el rango de tiempo y selecciona "Generar informe".

La vista previa del informe contiene secciones como detalles generales (título, fecha, sitio, rango de tiempo y registros seleccionados), 

y KPIs como el promedio del estado de Boulder, valor P, volumen promedio por hora, volumen total, tasa de producción en toneladas por hora, y porcentaje de cargas dentro y fuera del rango aceptable.

En la sección de productividad, puedes pasar el cursor sobre una línea para ver el volumen transportado por cada camión a lo largo del tiempo, 

junto con la distribución de tamaño de partícula.

Es posible seleccionar los valores P desde la esquina superior derecha para visualizar su comportamiento a lo largo del tiempo.

El gráfico de distribución de tamaño de partícula muestra la distribución agregada. Por defecto, se usa el modelo SW Breck, aunque puede cambiarse a Rosin, Rambler, o dejarlo sin modelo.

La tabla de valores P muestra el porcentaje de material más pequeño que un tamaño determinado. También hay una tabla y gráfico del tamaño objetivo.

Puedes modificar esta sección haciendo clic en "Agregar área de tamaño objetivo", incluyendo opciones como sesgo frontal, trasero, lateral y posición de carga.

La sinopsis muestra cómo se distribuyen las cargas en las distintas posiciones del camión: delantera, trasera y laterales.

También se incluye una sinopsis de cada registro de tamaño de partícula. Puedes ajustar el número de registros visibles haciendo clic en el área correspondiente.

Una vez listo, haz clic en “Descargar PDF” en la esquina superior derecha para guardar el informe localmente.

También se puede generar y descargar un archivo CSV. Para ello, haz clic en “Generar CSV”, y si deseas, activa la opción para incluir una columna de contenedores.

 Luego selecciona el rango de tiempo y haz clic en “Generar”. El archivo se descargará automáticamente.

Para acceder a la página de configuración de la cuenta, haz clic en el botón de menú ubicado en la parte superior derecha de la barra lateral, y luego selecciona “Configuración”.

La página de configuración de la cuenta está dividida en tres secciones principales.

Desde ahí, los usuarios pueden personalizar diferentes aspectos de MetricsManager Pro.

Una de las opciones disponibles es la medición de la página de inicio, donde se pueden ajustar las unidades de medición que se mostrarán.

También es posible seleccionar entre dos métodos: el método de tamaño sieve o el modelo de estimación de distribución del tamaño de partícula.

En el método sieve, se puede definir tanto el tamaño máximo como el tamaño mínimo, conocido como tamaño CIV.

Para determinar el tamaño máximo, se ajusta una elipse al contorno de la roca. Luego, se toma el cuadrado más pequeño que pueda encajar dentro de esa elipse como referencia.

Ese valor se utiliza como el tamaño mínimo sieve.

La elipse también permite calcular el diámetro menor, que se considera como el tamaño sieve en este contexto.

Por otro lado, el modelo de estimación simula la distribución del tamaño de las partículas, especialmente en el caso de partículas más finas, utilizando el modelo Swebrec.

Este modelo es el recomendado para su uso con MetricsManager Pro.

También puedes ajustar la configuración de fecha y hora de TruckMetrics, lo que permite cambiar la zona horaria o el formato en que se muestran estos datos.

Agradecemos tu tiempo y atención.

Aplicar lo aprendido contribuirá a mantener nuestros altos estándares y a mejorar continuamente nuestras operaciones.

Te invitamos a estar pendiente de futuras oportunidades de capacitación.

Recuerda que tu conocimiento es clave para nuestro éxito.

Ahora, tómate un momento para realizar nuestra prueba y poner en práctica todo lo que has aprendido.

Si necesitas ayuda o tienes alguna pregunta, no dudes en contactar a tu representante de Weir Motion Metrics o con el equipo de soporte.

Estamos aquí para ayudarte.


"""


# Generate Spanish TTS audio
tts = gTTS(text=spanish_script, lang='es')

# Save to MP3 file
output_file = "dubbing_output.mp3"
tts.save(output_file)

print(f"Audio dubbing saved as: {output_file}")
