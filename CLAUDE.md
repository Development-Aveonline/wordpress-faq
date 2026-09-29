# wordpress-faq — Guía operativa

> Idioma: el equipo trabaja en **español**.
> ⚠️ **Las reglas de la casa viven en `app-v2/.ai/nucleo/NUCLEO.md`** y se escriben acá
> automáticamente. **No las edites en este archivo** — un gate de la CI lo caza. Lo de *este*
> repo sí se edita acá.

Repositorio de contenido que convierte FAQs en `.docx` a JSON para consumo de WordPress; no es una
aplicación con runtime, servidor ni base de datos propia.

---

<!-- NUCLEO-AVEONLINE:INICIO — generado por `php spark harness:nucleo`. No editar acá. -->

## Reglas de AveOnline (núcleo compartido)

Estas reglas valen en **todos** los repos, sin importar el lenguaje o el stack. Lo específico de
este repo va fuera de este bloque.

### 0. La regla de oro

**Si algo no está en el código o en el harness, NO lo asumas — verifícalo o pregúntalo.** Varias
bases de datos de AveOnline son de producción y compartidas entre sistemas; asumir un esquema, una
columna o un comportamiento lleva a errores reales, no a un test rojo.

**Inicio ágil.** Acepta instrucciones breves. Busca por tu cuenta el issue de
Linear, el proyecto, el SPEC y los archivos pertinentes; lee solo lo necesario para esta tarea.
No pidas que el usuario reformule su prompt ni presentes un plan previo por defecto. Si el resultado
es verificable y se cumplen las puertas de seguridad de esta guía, ejecuta. Pregunta solo cuando
falte una decisión que cambie la solución o impida avanzar; haz una pregunta concreta y propone
una opción. No conviertas una preferencia menor en un bloqueo.

Comunica avances solo ante un hallazgo, un bloqueo, una decisión o una tarea larga; no narres cada
lectura o comando. La respuesta final por defecto ocupa 2–4 líneas: resultado, verificación y
próximo paso o bloqueo real, con la categoría de evidencia de la sección 4. Omite antecedentes,
planes ya ejecutados, detalles internos y advertencias hipotéticas. Amplía solo cuando el usuario
lo pida o un riesgo o decisión real lo exija; enlaza el issue o PR para los detalles. Para trabajo
paralelo, abre sesiones independientes solo si tienen alcance y archivos separables; identifica un
responsable de integrar y revisar cada una. Reutiliza el contexto ya leído; no repitas búsquedas o
pruebas sin un cambio o riesgo concreto.

**Modelo:** usa el modelo configurado para la sesión. La selección automática del modelo principal
requiere un lanzador o configuración externa; una instrucción en este archivo no lo cambia. Cuando
la herramienta permita elegir modelos para subtareas, reserva el modelo más capaz para problemas
complejos o de alto riesgo y usa uno más económico para tareas acotadas; no delegues por rutina.

**Memoria viva sin trabajo extra para el usuario.** En el mismo turno, registra toda corrección o
aclaración del usuario que cambie el trabajo: qué supuesto se corrigió, la decisión vigente, su
alcance y el issue o PR de origen. No pidas «guárdalo» ni hagas otra llamada de IA para resumirlo.
Guarda lo propio de la tarea en su issue o PR; lo estable del producto en el SPEC o documentación
del repo; lo que cambie una regla compartida en `.harness/mejoras/` según la sección 9. Antes de
escribir, busca el registro existente y actualízalo para evitar duplicados. Antes de una tarea nueva,
recupera solo las decisiones pertinentes, no el historial entero. No copies transcripciones,
secretos, datos personales ni suposiciones sin verificar. Una propuesta al núcleo no se convierte
en regla general hasta su revisión. Agrupa la captura con la actualización normal del trabajo. Si
el destino no está disponible, informa el registro pendiente.

**Toda solicitud a terceros queda en Linear en el mismo turno** *(decisión de Andrés, 28-sep-2026;
AVE-235, AVE-402)*. Cuando el agente redacta o envía un pedido a una persona, un equipo o un
proveedor —mensaje, correo, pregunta, cambio—, lo registra en Linear **en el turno en que entrega
el texto**, no al cerrar el tema ni cuando el usuario lo pida. Si hay issue, va como comentario ahí;
si no, se crea uno. Cada registro dice a quién se pidió —el nombre de trabajo y la organización o el
rol del destinatario interno o del proveedor, nunca su teléfono ni su correo—, qué, por qué canal y en
qué estado está:
`redactado — envío sin confirmar`, `enviado`, `respondido` o `cerrado`. Se actualiza en el turno en
que llega la confirmación o la respuesta. Las solicitudes abiertas con un mismo proveedor se agrupan
en un issue de seguimiento con casillas, enlazado a los issues de detalle. **Un issue nuevo se crea
sin responsable** y pasa por la puerta de investigación (AVE-235): el agente no lo asigna, ni
siquiera a quien lo pidió. No se registran secretos, datos de clientes (identidad, contacto o
texto crudo de sus conversaciones) ni datos personales sensibles. Por qué: el 28-sep, nueve pedidos a Meteor y Starsco pasaron horas
solo en el chat y se registraron todos juntos al final; mientras tanto, Linear mostraba un estado
que no era el real.

**Todo correo o mensaje de trabajo enviado abre un seguimiento hasta integrar la respuesta**
*(decisión de Andrés, 29-sep-2026; AVE-410; excepción expresa a la revisión previa de Juan o
Alejandro para esta regla)*. En el mismo turno del envío, el agente deja en el issue el canal, el
hilo o vínculo seguro, qué respuesta espera, el responsable de revisarla y el criterio de cierre;
no copia allí el texto crudo ni datos personales. Si cuenta con lectura autorizada y
automatización, activa un monitor verificable del hilo. Mientras no haya una respuesta útil,
permanece abierto y guarda silencio si no cambió nada. Al recibirla, contrasta lo respondido con
lo pedido, distingue hechos de estimaciones y actualiza el issue, SPEC, bitácora, decisiones,
código o producto que correspondan; verifica el efecto en cada consumidor afectado. Una
respuesta parcial no cierra el seguimiento. Antes de cerrarlo, registra la evidencia integrada y
comprueba que no quede un dato o decisión pendiente. No envía recordatorios adicionales sin la
autorización correspondiente. Si no puede leer la respuesta, mantener un monitor o aplicar un
cambio, informa la limitación y pide la intervención concreta; nunca promete seguimiento o
actualización que no haya configurado y comprobado.

**Recuperación verificable de aprendizajes y QA.**
Al iniciar, retomar o compactar, recuperar el SPEC, las decisiones vigentes, la bitácora y la
evidencia pertinente del proyecto. Consolidar cada corrección en el mismo turno con supuesto
sustituido, decisión vigente, alcance, issue o PR y aceptación verificable; actualizar también
los consumidores afectados. Conservar historia sin crear fuentes rivales. Al rediseñar,
contrastar código y recorridos actuales antes de declarar paridad. Al cerrar, conciliar pedidos,
cambios, pruebas y bloqueos. Los hooks solo recuerdan esta obligación; no demuestran por sí
solos el cumplimiento. Vincular evidencia a versión, corte y población; probar fallos esperados
e invalidar resultados obsoletos. Distinguir DEMO, verificación local, QA real y producción.
No afirmar propagación a otros repos sin versión, PR y prueba; no copiar prompts, datos de
clientes ni transcripciones como memoria.

### 1. Secretos

- **NUNCA commitear `.env`** ni ningún archivo con credenciales, llaves o tokens.
- **No reproducir secretos** en respuestas, mensajes de commit, logs ni capturas — ni siquiera
  parcialmente, ni "para verificar".
- Si un secreto quedó expuesto, **decirlo de inmediato**. Rotarlo es del dueño del sistema; callarlo
  no es una opción, y esconderlo cuesta más que el error.

### 2. Todo trabajo pertenece a un proyecto, y todo proyecto a un SPEC

En AveOnline no se desarrolla ni se resuelve un soporte "suelto". **Antes de escribir código se
declara a qué proyecto pertenece el trabajo**; si no existe, se crea.

- Un arreglo reactivo **también** pertenece a un proyecto, no es una excepción a la regla.
- Si el usuario no lo declara, busca primero el issue, el proyecto y el SPEC existentes. Vincula
  el trabajo cuando haya una correspondencia clara. Si no la hay, registra o actualiza el issue en
  Triage con la evidencia y una propuesta de clasificación; sigue investigando lo que no dependa
  de esa decisión. El agente gestiona esta clasificación: no pidas al usuario el nombre del
  proyecto. Pregunta solo por el resultado de negocio si tampoco puede inferirse.

**2.1 · Antes de declarar el proyecto, traé el contexto del Brain.** *Recomendado, no obligatorio.*
El repo dice qué se planeó; el estado vivo, las capacidades reales y los permisos por rol están en
el Brain. Declarar un proyecto leyendo solo los archivos del repo es planear a ciegas, y ya mordió:
**el 19-ago-2026 se reportaron «14 tareas en revisión» leyendo un archivo de plan mientras la
fuente viva mostraba 7**. Los dos números eran correctos según su fuente, y con esos números se
decidió a qué dedicarle el día.

Se trae con `mcp__brain-aveonline__brain_load_context`. **Si el MCP no responde, se sigue con el
catálogo del repo y se dice explícito** que el proyecto se declaró sin el contexto del Brain: eso
no puede quedar invisible. *(En `app-v2` esto además tiene gate; en el resto es la recomendación.)*

**2.2 · Todo proyecto apunta a un SPEC, y el SPEC vive en `app-v2`.** Antes de empezar se apunta a
uno existente o **se crea uno nuevo** — no hay tercera opción.

Los proyectos de AveOnline están centralizados en `app-v2/proyectos/<nodo>/<proyecto>/`, y ahí vive
su `spec.md` junto a su `bitacora.md`. **Vale para el trabajo de cualquier repo:** la tarea se hace
donde vive el código, pero el proyecto y su SPEC son únicos y están en un solo lugar. Cómo se
escribe cada sección y con qué rúbrica se revisa: `app-v2/proyectos/_plantilla/GUIA-SPEC.md`.

**El SPEC es la fuente del alcance.** Dice **por qué, hasta dónde, y cómo se sabe que terminó** —
contexto, decisiones de arquitectura, tareas con sus criterios y definición de hecho. Sin él, seis
semanas después nadie puede reconstruir por qué el alcance era ese, y la discusión se vuelve a dar
desde cero.

**2.3 · El SPEC se publica y revisa antes del código productivo.** No basta con que exista en la
máquina de quien implementa. Antes de editar código de producto, el SPEC debe:

- estar validado contra `proyectos/_plantilla/GUIA-SPEC.md`, sin placeholders ni secciones
  obligatorias vacías;
- tener un PR propio en `app-v2`, separado del PR de implementación, y estar enlazado desde la
  incidencia canónica de Linear;
- reconciliar trabajo previo en Linear, Azure, GitHub y producción, preservando lo ya resuelto y
  declarando únicamente la brecha residual;
- estar revisado antes de empezar implementación cuando el riesgo sea alto o crítico.

El PR separado protege el orden de las decisiones: revisar alcance después de escribir código
convierte cada corrección en retrabajo y facilita que dos personas resuelvan lo mismo. **Un merge del
SPEC no autoriza por sí solo un despliegue ni cierra la acción.**

La única excepción es un incidente productivo activo donde esperar agrava daño real. En ese caso se
abre primero la incidencia, se registra alcance provisional y rollback, y el SPEC se publica en el
mismo ciclo antes de declarar CÓDIGO LISTO. La urgencia no permite omitir evidencia ni reconciliación.

> **El gestor de proyectos se retiró de `app-v2` el 12-sep-2026** (`[GESTOR#T23]`, PR #888): ya no
> hay `proyecto.yml`, ni tablero, ni token de commit, ni señales. **El SPEC quedó como la única
> fuente de verdad del alcance**, y por eso su lista de tareas dejó de ser un resumen del plan para
> pasar a ser el plan. Si algún día vuelve a haber tablero, se alimenta del SPEC.

### 3. Commits

- **En español**, con prefijo `Feat:` o `Fix:` (o `Docs:`, `Chore:`).
- **Sin token de tarea.** El `[PROYECTO#Tn]` existía para alimentar el tablero del gestor; retirado
  el gestor, no hay quién lo lea. Un commit que lo lleve no rompe nada, pero ya no significa nada.
- **Doble co-autor** al final del mensaje:
  ```
  Co-authored-by: Aveonline Brain <brain@aveonline.co>
  Co-authored-by: Claude Opus 4.8 <noreply@anthropic.com>
  ```
- **Nada de `git add -A` a ciegas.** Se agrega solo lo que se cambió a propósito.
- El mensaje explica **por qué**, no solo qué. Un commit que dice "arregla el bug" obliga a alguien,
  meses después, a reconstruir el razonamiento desde el diff.

### 4. Cómo se reporta el avance (regla 11 del arnés)

**Prohibido decir "listo" o "funcional" sin verificación end-to-end.** Todo reporte usa una de tres
categorías, explícitamente:

| Categoría | Qué significa | Qué NO significa |
|---|---|---|
| **CÓDIGO LISTO** | Escrito, pasa lint y pruebas | Que alguien pueda usarlo |
| **DESPLEGADO** | En producción, deploy verificado | Que la interfaz lo invoque |
| **VERIFICADO END-TO-END** | Alguien con el rol real lo usó desde la interfaz real | — |

Antes de usar la tercera, confirmar las tres dependencias que más fallan **en silencio**:
**(a)** el frontend invoca el endpoint nuevo, no solo existe en el backend; **(b)** la migración de
esquema ya corrió en el ambiente real, no "está lista para correr"; **(c)** la sesión, el rol y el
permiso están confirmados, no asumidos.

Si una superficie no se pudo verificar, **se dice cuál y por qué** — nunca se omite.

> **El verde del CI no es evidencia.** Un gate solo prueba algo si además se verificó que **falla
> cuando debe fallar**. Un verde que nunca se puso en rojo no protege nada, y se lee igual que uno
> que sí protege.

**4.1 · La etiqueta y el nivel de evidencia son dos ejes, no uno** (aceptado del buzón de mejoras,
`mejora_harness_20260827.md`, M1/M1-bis). La categoría (CÓDIGO LISTO / DESPLEGADO / VERIFICADO
END-TO-END) describe la **etapa**. El nivel de evidencia describe **qué tan buena es la prueba**, y
son independientes: se puede estar en DESPLEGADO con evidencia apenas N1.

| Nivel | Qué es |
|---|---|
| **N1** | Demostración — corrió una vez, en un ambiente controlado |
| **N2** | Logueado con datos reales que persisten **y se releen del backend** — no solo se vieron en pantalla |
| **N3** | Alguien con el rol real lo usó desde la interfaz real y firmó pasa o falla |

**"Asegurado" a secas queda prohibido.** Todo reporte declara el nivel alcanzado **y qué no se
probó**.

**N2 se verifica, no se declara:** el cierre exige la relectura en forma reproducible — la consulta o
el comando, y su resultado — y algo la vuelve a ejecutar antes de aceptar el cierre. Una captura de
pantalla es una afirmación; el resultado de una consulta reproducible es un dato que se puede volver
a producir.

**La etiqueta VERIFICADO END-TO-END no se escribe a mano.** Se deriva: existe la prueba por rol de
esa funcionalidad, corrió, pasó, y su relectura volvió con el dato. Mientras eso no se cumpla, la
etiqueta no se puede declarar.

**N3 es irreducible — ningún mecanismo verifica que una persona con el rol real miró una pantalla.**
Se cubre con dos cosas, y ninguna es un gate:
- **Auditoría por muestreo:** una tarea cerrada como VERIFICADO por semana, elegida al azar,
  re-verificada por otra persona.
- **Quién paga:** quien declaró VERIFICADO **recibe automáticamente asignado el issue** si se
  reabre. No es sanción — el trabajo vuelve a donde salió.

Las dos piezas de N3 se encienden **el mismo día**, nunca en secuencia (encenderlas por partes se lee
como vigilancia que después castiga). Aplican sin excepción — Alejandro, Juan, el agente cuando
cierra una tarea, y quien lo propuso. Se anuncian antes de encenderse, con el porqué.

**4.2 · Un traspaso entre roles se prueba como traspaso, no como dos pantallas sueltas** (M2). Si una
funcionalidad hace que el rol A actúe y el rol B tenga que verlo (una solicitud, una aprobación, una
novedad), no cierra sin una prueba que cubra el traspaso completo: A actúa → B lo ve. Depende de 4.3.

**4.3 · Cuentas canónicas por rol, con datos sembrados a su nombre** (M3, prerrequisito de 4.1, 4.2 y
la regla 6.7). Cada rol real del sistema tiene una cuenta de prueba canónica, y el sembrado enlaza
esa cuenta a su registro y siembra el flujo a su nombre — no una cuenta genérica. Un humo por rol:
cada rol entra y su bandeja principal da más de cero filas, o queda escrita la razón de por qué no.

### 5. Seguridad y QA

1. **Sin migración versionada no hay DDL.** Ninguna alteración de esquema por `ALTER`/`CREATE`/`DROP`
   suelto, ni con confirmación del usuario: la confirmación no reemplaza la migración.
2. **Sin blindaje de tests no se toca facturación, cartera, billetera ni transportadoras.**
3. **Mapa de dependencias antes de tocar un módulo core.** Con herramienta, no con "creo que nada
   más lo usa".
4. **Gates de CI/CD bloqueantes**, sin excepción "por esta vez".
5. **Human-in-the-loop** en módulos core: revisión línea por línea, y prueba de rollback antes de
   un cambio de esquema en producción.
6. **Veracidad entre tablas:** un mismo hecho de negocio no puede tener valores distintos en tablas
   distintas. Todo dato replicado queda cubierto por una prueba de reconciliación.
7. **Los errores nunca son silenciosos** (M5). El QA de navegador escucha `pageerror` y
   `unhandledrejection` y **falla** si aparece cualquiera — no basta con afirmar que ciertos textos
   están en pantalla, porque un error de JavaScript que no cambia el marcado visible pasa en verde.
   Prohibido un `catch` vacío o un `return null` silencioso alrededor de una escritura de red **sin
   mostrar el estado** al usuario.
8. **Toda escritura con identidad deja rastro, y el rastro se verifica releyendo** (M7). Tras una
   acción que registra quién la hizo, se relee para confirmar que las columnas de rastro (autor,
   fecha) quedaron correctas — con el identificador de usuario **del token de sesión, nunca del
   cuerpo de la petición**. Un `200` no es evidencia; la relectura sí.
9. **Un gate no se acepta sin su rojo, y el rojo queda registrado** (M8). El rojo de prueba de un
   gate es un artefacto registrado, no una afirmación en un comentario: qué mutación se inyectó, qué
   código de salida dio, y en qué corrida. Un gate sin eso no se acepta como protección.
10. **Un hallazgo de un agente de IA es un candidato, no una verdad** (M9, extiende
    `restricciones-agente-ia.md` §3). Todo hallazgo automático lleva el campo **"reproducido en
    vivo: sí/no"**, y solo un "sí" puede cerrar un issue. Toda regla basada en patrones (grep,
    matcher) declara cómo se midió su cobertura — forzando la condición en vivo, no contando
    coincidencias del propio patrón, porque un matcher falla de dos formas y el falso negativo se ve
    exactamente igual que un verde legítimo.

### 6. Dónde vive cada cosa

- **Investigación y el "por qué"** → el monorepo de investigación (`Brain_Avemetrics_Aveonline`).
- **Estado operativo de un sistema** → junto a su código.
- **Toda tarea = issue/tarea en el repo real**, nunca en el repo de investigación.
- **Sin fechas de calendario** en las tareas: se etiqueta por fase lógica.
- **Antes de abrir una tarea, verificar que no exista ya una equivalente.**

### 7. La documentación es parte del cambio

Tras un cambio significativo se actualiza **en el mismo flujo de trabajo**, no después: el
`CHANGELOG.md`, la doc del área afectada y el estado del proyecto. **No dejar el código adelantado
a los docs.**

Y un doc **no puede afirmar cifras o estados que el código desmiente**. Cuando una afirmación es
verificable (cuántos comandos hay, cuántas pruebas corren, qué está encendido), lo durable es un
gate que la compare contra la realidad — corregir el número a mano se vuelve a desfasar en el
siguiente cambio.

### 8. Interfaz y datos

Toda vista con **etiquetas (KPIs), tablas o indicadores** cumple el estándar único de AveOnline
(`ESTANDARES-AVEONLINE.md`). Lo esencial:

- **Sistema de diseño único: [AveDS](https://github.com/Development-Aveonline/AveDS).** Se usan
  **tokens**, nunca colores, sombras o tipografías hardcodeadas. **Si falta un token, NO se inventa
  — se toma de AveDS.**
- **Tablas del sistema:** ordenables por encabezado, con filtro por columna, fila de TOTAL cuando
  hay algo real que sumar, export y drill al detalle. Nada de tablas crudas.
- **KPIs** que abren el detalle que agrupan, comparan contra un período anterior y traen semáforo.
- **Lectura visual y detalle universal (decisión de Andrés, 25-sep-2026; AVE-249).** En todo
  AveOnline, la entrada permite interpretar situación, tendencia, riesgo y próxima decisión de
  un vistazo. Cada KPI, insight, alerta y elemento de una gráfica abre un modal con el conjunto
  exacto que lo sustenta; desde allí se llega a la ficha y evidencia autorizadas. Los niveles tienen
  «Volver» y conservan período, filtros, selección, posición y foco. Filtros visibles y removibles;
  tablas completas al profundizar. El modelo agéntico explica evidencia, incertidumbre, propuesta,
  acción existente y verificación; no confunde recomendar con ejecutar. Si falta el detalle, se
  declara pendiente: no se simula ni se presenta un agregado como registros individuales.
  Revisión obligatoria: recorrido con teclado, conciliación indicador/detalle, regreso con contexto,
  permisos en cada nivel y conservación de funciones anteriores. Registrar brechas en trabajo
  existente; no declarar cumplimiento global porque una pantalla pase. Contrato completo:
  `app-v2/BrainAve/ESTANDARES-AVEONLINE.md`, sección 4.1.
- **Período por defecto = mes en curso.**
- **Filtro visible y removible:** al filtrar debe verse qué filtro está activo y cómo quitarlo.
- **Antirregresión:** al portar o reescribir una pantalla no se pierden funciones del original, y
  eso se asevera en las pruebas.
- **Un dato de ejemplo se declara como tal, al lado del número.** Un aviso global no acompaña al
  número: la persona hace scroll y ya no lo ve.
- **Ningún dato de demostración es presentable como real** (M4, endurece el punto anterior). Al
  arrancar con credenciales reales, falla si aparece cualquier centinela de demostración declarado.
  Y se verifica el caso que de verdad importa: forzar en vivo que la llamada real devuelva nulo, por
  vista, y afirmar que aparece un aviso de reintentar — **nunca** que la vista se quede mostrando el
  dato de demostración como si fuera real (el patrón `if (api) VAR = api.map(...)`: si el endpoint
  falla, `api` es nulo, no entra al `if`, y la demostración queda en pantalla sin decir que lo es).
- **Lo que la interfaz ofrece coincide con la matriz de permisos** (M6, desbloquea las reglas A2/A6
  del arnés de guardarraíles). Si una vista de un rol invoca un recurso que ese rol no tiene en la
  matriz (rol × recurso), es rojo — no basta con que el backend rechace la llamada; la vista no debe
  ofrecer el flujo en primer lugar.

### 9. Cómo se propone una mejora al harness

**El núcleo no se edita donde lo leés.** Está entre marcas y se regenera desde una fuente única, así
que un cambio hecho ahí se pierde en la siguiente corrida y el gate de la CI lo marca en rojo. Eso
es a propósito: es lo que impide que existan cuarenta versiones distintas de la misma regla.

Pero una regla equivocada tiene que poder corregirse, y quien la detecta casi nunca es quien
mantiene el harness. **Para eso está el buzón:**

```
.harness/mejoras/mejora_harness_AAAAMMDD.md
```

Se crea en **el repo donde apareció la necesidad**, sin pedir permiso y sin abrir una discusión.
Si ya hay uno con esa fecha, se agrega un sufijo: `mejora_harness_20260820_2.md`.

Cada archivo dice, sin adornos:

- **Qué regla** — la del núcleo que estorba, falta o está mal.
- **Qué pasó** — el caso concreto que lo destapó. Sin un caso real es una opinión, y las opiniones
  no cambian una regla que aplica a toda la organización.
- **Qué proponés** — el texto nuevo, si lo tenés.
- **Qué se rompe si se aplica** — a quién le cambia el trabajo. Si no se te ocurre nada, decilo:
  esa respuesta también informa.

**Los revisan Juan o Alejandro** —cualquiera de los dos—, deciden y actualizan la fuente. Proponer
no es aplicar: que un archivo exista no cambia ninguna regla hasta que se acepta y se regenera.

Que sean dos y no uno es deliberado: un buzón con un solo dueño se atasca la primera semana que esa
persona está ocupada, y a partir de ahí la gente deja de escribir. Y **se responde también cuando se
rechaza, con el motivo** — un buzón donde las cosas entran y nunca sale nada deja de usarse a la
tercera vez.

Escribirlo en el momento es la mitad del valor. Una mejora que se posterga "para cuando haya
tiempo" se pierde, y la siguiente persona vuelve a chocarse con lo mismo sin saber que ya le pasó a
alguien.

### 10. Paridad `CLAUDE.md` / `AGENTS.md`

Los dos archivos dicen **las mismas reglas**: `AGENTS.md` existe para las herramientas de
codificación que no leen el otro. **Se generan del mismo fuente y reciben texto idéntico**, así que
la paridad no depende de que alguien se acuerde de replicar un cambio.

Por eso este núcleo está escrito **sin nombrar ninguna herramienta**: dice "el agente". Lo
específico de una (sus comandos, sus atajos) va en la parte local de cada archivo, nunca acá.

<!-- NUCLEO-AVEONLINE:FIN -->

---

# Lo que es cierto SOLO de este repo

## Qué es y de qué depende

Repositorio de contenido: convierte FAQs en `.docx` (español) a archivos JSON `pregunta`/`respuesta`
consumidos por WordPress. No es una aplicación con runtime propio — no hay servidor, framework web
ni endpoint en este repo.

- **Script:** `extract.py` — Python 3, solo librería estándar (`zipfile`, `xml.etree.ElementTree`,
  `json`, `os`, `re`). Parsea el XML interno del `.docx` (`word/document.xml`) directamente; **no**
  usa `python-docx` pese a que `AGENTS.md` lo mencionaba como opción.
- **Entrada:** `faq/*.docx` (12 documentos Word en español).
- **Salida:** `json/*.json` (uno por documento) + `faq.json` en la raíz (agregado de todos).
- **`package.json`** es un placeholder: sin dependencias, `"test"` solo hace `exit 1`.
- **Quién depende de él (WordPress u otro sistema que consuma estos JSON):** no verificable desde
  este repo — no hay referencia a una URL, API o job de importación.

> **TODO:** confirmar quién/qué consume `json/*.json` o `faq.json` (¿un plugin de WordPress, un
> import manual, un webhook?) y con qué frecuencia se espera que se actualice.

## Base de datos

No usa base de datos. No hay configuración de conexión, ORM, ni credenciales en el repo.

## Deploy

No hay `.github/workflows/` ni ningún otro pipeline de CI/CD en el repo (verificado: el directorio
`.github` no existe). No hay evidencia de deploy automático — el único commit visible (`fix`,
25-jun-2026, Francisco Blanco) fue directo a `master`.

> **TODO:** confirmar si `master` dispara algo fuera de este repo (por ejemplo, un pull manual desde
> WordPress) — no hay rastro de eso acá.

## Cómo se prueba

No hay suite de pruebas. `package.json` declara `"test": "echo \"Error: no test specified\" && exit 1"`
como placeholder. `AGENTS.md` (antes de este cambio) decía explícitamente "no README, no CI, no
linters, no formatters, no tests in this repo" — con el gate de este PR el repo pasa a tener CI por
primera vez (el gate del núcleo), acotado a `CLAUDE.md`/`AGENTS.md`.

## Convenciones propias

Contrato de conversión `.docx` → JSON (de `AGENTS.md`, preservado):

- Cada `.docx` en `faq/` genera un `.json` homónimo en `json/` con el formato:
  ```json
  [{ "question": "string", "answer": "string (puede tener HTML)" }]
  ```
- Los links dentro de `answer` van como:
  `<a href="url"><span style="font-weight: 400">url</span></a>`
- Las listas dentro de `answer` van como:
  `<ul><li>Item 1</li>...</ul>`
- `[NOMBRE_MUNICIPIO]` se reemplaza por `{{nombre_municipio}}`.
- Documentos fuente: binarios `.docx` en español — se extraen con `zipfile` + XML (ver `extract.py`),
  pese a que el texto original de `AGENTS.md` sugería `python-docx` "o equivalente".
- Sin convención de branching: commit único directo a `master`.

## Trampas conocidas

> **TODO:** esta sección la escribe quien conoce el sistema. Es la más valiosa del harness —cada
> cosa que ya mordió a alguien, con el síntoma que se vio y la causa real— y no se puede deducir
> leyendo el código. No hay nada documentado en el repo que permita completarla sin adivinar.
