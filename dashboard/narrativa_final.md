# 💧 Agua y Pobreza: La Trampa Rural
**Narrativa de Datos y Storytelling - Proyecto HackODS UNAM 2026**
**Equipo:** linuxitOS (Jesus Sebastián Vázquez Zarco, Alejandra Naomi Muciño Hernández, Victor Federico Caldera Arellano)

---

## 📌 El Corazón de Nuestra Historia

El cruce entre el **ODS 1 (Fin de la Pobreza)** y el **ODS 6 (Agua Limpia y Saneamiento)** no es una simple correlación estadística; es la radiografía de una condena estructural. 

Nuestra premisa fundamental es que **la pobreza va más allá de la falta de ingresos; es la carencia de los servicios básicos que permiten una vida digna**. El acceso al agua potable no es un lujo, es el cimiento sobre el cual se construye la salud, el tiempo libre para educarse y la capacidad de generar sustento. Quien carece de agua, está encadenado a la pobreza extrema.

Esta narrativa está construida en 4 actos diseñados para guiar al usuario del dashboard a través de los datos duros (INEGI, CONEVAL, CONAGUA), revelando el rostro humano detrás de las estadísticas.

---

## ACTO 1: La Ilusión Nacional (El Espejismo de los Promedios)
*Esta sección abre el dashboard. Su objetivo es romper el mito de que "vamos por buen camino" basándonos en datos nacionales o estatales.*

### La Narrativa (Propuesta para el Dashboard)
El Estado Mexicano reporta a la comunidad internacional que aproximadamente el 64% de la población cuenta con agua potable gestionada de forma segura (Indicador 6.1.1.a del SIODS). Sin embargo, cuando observamos los mapas a nivel de Entidad Federativa, todo parece "aceptable". Esta estadística a gran escala es un **espejismo**.

La riqueza y la vasta infraestructura de las grandes capitales urbanas "promedian hacia arriba" a todo el estado, borrando estadísticamente a las comunidades vulnerables. Un promedio estatal no quita la sed. Cuando un sistema de medición no desciende a nivel municipal o de localidad, condena a la invisibilidad a millones de personas cuyas llaves de agua llevan años secas. Para encontrar la verdad, tuvimos que romper la ilusión y profundizar en los microdatos de 2,469 municipios.

---

## ACTO 2: La Realidad Demográfica (La Condena de la Distancia)
*Esta sección contextualiza el verdadero reto logístico de México. No es solo que falte agua, es a quiénes les falta.*

### La Narrativa (Propuesta para el Dashboard)
El Censo de Población y Vivienda 2020 del INEGI revela una dualidad paralizante: aunque solo una minoría de los mexicanos vive en zonas rurales (localidades de menos de 2,500 habitantes), **más del 55% de los municipios del país** tienen esta clasificación. 

Esta inmensa dispersión geográfica representa el verdadero obstáculo logístico y político para el ODS 6. Entubar agua para 10,000 personas agrupadas en una sola colonia urbana es rápido y políticamente rentable. Llevar agua a 50 comunidades dispersas en la sierra requiere una voluntad política y una inversión diametralmente mayores. La lejanía se convierte en un castigo: las políticas públicas priorizan el volumen sobre la equidad, dejando atrás a quienes ya están geográficamente aislados. La distancia física se ha traducido en distancia social.

---

## ACTO 3: La Trampa de Infraestructura (El Clímax de la Desigualdad)
*Esta es la sección de los gráficos de dispersión (Scatter Plot). Aquí demostramos matemáticamente la correlación entre ODS 1 y ODS 6.*

### La Narrativa (Propuesta para el Dashboard)
Los números oficiales son brutales e irrefutables. Existe una **brecha de desigualdad de 4.6x**: un municipio rural tiene casi cinco veces más probabilidades de no tener agua entubada que uno urbano. 

Al cruzar la infraestructura hídrica (CONAGUA) con las mediciones multidimensionales de pobreza (CONEVAL), surge un patrón innegable: **a mayor carencia de agua, mayor pobreza extrema**. Esta es "La Trampa Rural". La falta de agua es, a la vez, síntoma y causa de la miseria. El tiempo que dedican las familias rurales (históricamente mujeres y niñas) a acarrear agua, es tiempo robado a la educación o al trabajo remunerado. Las enfermedades gastrointestinales merman la precaria economía familiar. Es matemáticamente imposible salir de la pobreza extrema cargando cubetas.

---

## ACTO 4: La Comprobación Matemática (El Veredicto Final)
*El cierre del dashboard, donde analizamos los datos a nivel de cuenca hidrológica (RHA) y damos nuestro llamado a la acción.*

### La Narrativa (Propuesta para el Dashboard)
Al agrupar los datos por Región Hidrológico-Administrativa (RHA), comprobamos que, sin importar en qué zona del país nos encontremos —sea el árido norte o el lluvioso sur—, el patrón de abandono rural es una constante sistémica. La "Ilusión Nacional" queda completamente desmentida.

La intersección de los ODS 1 y 6 nos dicta un veredicto claro: ninguna transferencia de efectivo ni programa de asistencia social erradicará la pobreza extrema si no hay una llave de agua potable en casa. La infraestructura hídrica no es un tema exclusivo de ingeniería o tuberías; es el pilar más básico de la justicia social. Visibilizar esta trampa municipal es el primer paso para exigir que las políticas públicas dejen de promediar y empiecen a focalizar en quienes la geografía ha invisibilizado.

---

## 💡 Recomendaciones Estratégicas para el Equipo (linuxitOS):

1. **El Rostro Humano Primero:** Frente a los jueces, hablen de personas, no de "datasets" o "variables". Un dato es solo un número hasta que explican que ese 9.6% de carencia rural significa familias sin agua para lavarse las manos, cocinar o beber de forma segura.
2. **Defiendan su Metodología:** Recalquen que su mayor aportación técnica fue **romper el sesgo del promedio estatal**. El cruce municipal INEGI + CONAGUA + CONEVAL es su carta fuerte técnica y argumentativa.
3. **El Título del Proyecto:** "Agua y Pobreza: La Trampa Rural" es un título poderoso. Úsenlo en su discurso inicial y de cierre ("Hoy venimos a demostrarles cómo funciona la Trampa Rural y cómo podemos visibilizarla para romperla").
