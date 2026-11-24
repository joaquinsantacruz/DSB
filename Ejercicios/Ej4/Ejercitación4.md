![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

Ejercitación 4

Brownie

Subasta de sobre cerrado con commit–reveal

Objetivo

Desarrollar un contrato inteligente de subasta utilizando Solidity y Brownie. Los participantes

registrarán una oferta oculta mediante un compromiso criptográfico y luego la revelarán. Al

finalizar los plazos, el contrato determinará el ganador, registrará la adjudicación y permitirá

retirar los fondos sin intervención discrecional del vendedor. Si se utiliza un NFT, también

permitirá reclamarlo.

Alcance

Se implementará una única subasta por contrato para un bien o lote identificado mediante

una descripción o referencia. Su representación mediante un NFT ERC-721 es opcional,

implementar un ERC-721 no forma parte de la evaluación. Sin NFT, el contrato registrará la

adjudicación on-chain.

El mecanismo commit–reveal oculta temporalmente las ofertas: luego de revelarlas serán

públicas. Cada participante deberá realizar dos transacciones y conservar su secreto. El

depósito fijo inmoviliza capital y limita el importe máximo de la oferta.

Configuración y etapas

El vendedor, la descripción o referencia del bien, el depósito fijo D > 0 (en wei) y los

instantes de inicio, cierre de compromisos y cierre de revelaciones serán fijados antes de

comenzar y no podrán modificarse. Si se utiliza un NFT, también se fijarán su contrato y

tokenId. Debe cumplirse: inicio < cierreCommit < cierreReveal.

Si se utiliza un NFT, deberá estar en custodia del contrato antes del inicio, no se podrán

recibir compromisos sin verificar esa custodia. Sin NFT, no se requiere custodia de un activo

on-chain. No habrá cancelación ni reinicio de la subasta una vez habilitada.

Compromiso: inicio ≤ block.timestamp < cierreCommit.

Revelación: cierreCommit ≤ block.timestamp < cierreReveal.

![](data:image/png;base64...)

Finalización: block.timestamp ≥ cierreReveal. Las operaciones fuera de su etapa deberán

revertir.

Requisitos funcionales

1.  Cada wallet, excepto el vendedor, podrá registrar un único compromiso y deberá

enviar exactamente D. Un segundo compromiso deberá revertir, no se permitirán

reemplazos.

2.  El compromiso será keccak256(abi.encode(block.chainid, address(this), msg.sender,

oferta, secreto)). Los tipos y el orden son: uint256 chainId, address contrato,

address participante, uint256 oferta y bytes32 secreto. La oferta se expresa en wei.

Los scripts deberán reproducir exactamente esta codificación. No usar

abi.encodePacked.

3.  Cada participante generará un secreto aleatorio de 32 bytes fuera de la cadena y lo

conservará localmente hasta revelar. No deberá publicarlo anticipadamente ni

incluirlo en el repositorio. El contrato guardará el hash y el orden correlativo de

registro, no la oferta ni el secreto durante el compromiso.

4.  La revelación no requerirá enviar fondos. Solo se aceptará una revelación válida por

participante, con compromiso existente, secreto correcto y 0 < oferta ≤ D. Un

intento inválido deberá revertir sin impedir una revelación correcta posterior dentro

del plazo.

5.  Ganará la mayor oferta válida. Ante empate, tendrá prioridad el compromiso

registrado primero, independientemente del orden de revelación. El mejor candidato

deberá actualizarse al revelar.

6.  Cualquier dirección podrá ejecutar finalize después del cierre de revelaciones. Solo

podrá finalizarse una vez. La finalización fijará el resultado y registrará la

adjudicación al ganador, si existe, sin transferir fondos ni, cuando corresponda, el

NFT y sin recorrer participantes.

7.  Después de finalizar, cada participante que reveló correctamente podrá retirar D,

salvo el ganador, que retirará D − ofertaGanadora. Si el importe es cero, no tendrá

saldo a retirar.

8.  Quien no haya revelado válidamente al cerrar la etapa perderá D, que se acreditará

al vendedor. Una revelación inválida no cuenta como válida. Esta penalidad es una

regla explícita del ejercicio.

9.  El vendedor podrá retirar ofertaGanadora + (cantidadCompromisos −

cantidadRevelacionesValidas) × D; sin ganador, ofertaGanadora = 0. Cada depósito

se contabilizará una sola vez. Los retiros de participantes y vendedor serán

independientes y no podrán superar los derechos de cada uno.

10. Si se utiliza un NFT, el ganador podrá reclamarlo en una operación separada. Sin

ofertas válidas, lo reclamará el vendedor. Solo el beneficiario podrá solicitarlo y elegir

una dirección receptora no nula. Un receptor que rechace el NFT no deberá bloquear

la finalización ni los retiros de dinero. No se podrá reclamar dos veces. Sin NFT,

![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

11. bastará con registrar y permitir consultar la adjudicación o la ausencia de ofertas

válidas.

12. Todos los retiros de fondos serán individuales, posteriores a la finalización y de costo

O(1) respecto de la cantidad de participantes. El titular podrá indicar un receptor no

nulo. Deben evitarse reentradas y retiros dobles, una transferencia fallida deberá

revertir sin perder el saldo.

13. Se deberá registrar y permitir consultar la configuración, compromisos, orden de

registro, revelaciones válidas, cantidades necesarias para liquidar, ganador, oferta

ganadora, adjudicación y derechos ya cobrados. Si se utiliza un NFT, también se

registrará si ya fue reclamado. No se exigirá almacenar ni recorrer un listado global

de participantes.

14. Se emitirán eventos de compromiso, revelación, finalización y retiro de fondos. Si se

utiliza un NFT, también de su reclamación. Deben permitir reconstruir participantes,

orden y resultado de la adjudicación. No se publicará la oferta ni el secreto antes de

la etapa de revelación.

![](data:image/png;base64...)

UNLP. Facultad de Informática.

Desarrollo de Software para Blockchain

Cursada 2026

Entrega, pruebas y documentación

1.  Desarrollar scripts Brownie de deploy parametrizados por red y de interacción para

comprometer, revelar, finalizar y retirar fondos. Si se utiliza un NFT, incluir además la

configuración de su custodia y su reclamación. Fijar las versiones utilizadas en la

documentación del proyecto.

2.  Realizar el deploy en al menos una testnet pública, no solo en una red local. Publicar

red, chainId, direcciones de contratos y transacciones de una ejecución completa.

Utilizar exclusivamente fondos de prueba.

3.  Implementar y ejecutar los scripts de verificación del código fuente en Etherscan o

en el explorador compatible de la red elegida. Incluir los enlaces a los contratos

verificados.

4.  Desarrollar tests y mocks con Brownie y alcanzar al menos 80 % de cobertura del

contrato de subasta. Adjuntar el reporte y aclarar las exclusiones. La cobertura no

reemplaza los casos obligatorios.

5.  Probar: configuración inválida, límites exactos de cada etapa, segundo compromiso,

depósito incorrecto, vendedor participante, hash, secreto o remitente incorrectos,

oferta cero o mayor que D, doble revelación, recuperación tras un intento inválido,

empate con orden de revelación invertido, finalización por un tercero y finalización

repetida. También probar la ausencia de compromisos, la ausencia de revelaciones

válidas, un ganador con oferta D, las penalidades por no revelar, los retiros en

distinto orden, los retiros dobles, las llamadas no autorizadas, un receptor que

rechaza ETH, los intentos de reentrada y el registro y consulta de la adjudicación. Si

se utiliza un NFT, probar además la custodia inválida, las reclamaciones dobles, un

receptor que rechaza el NFT y la recuperación por el vendedor sin ofertas válidas. Un

fallo de un receptor no deberá bloquear a los demás.

6.  Verificar la contabilidad con múltiples participantes: suma de derechos de

participantes + derecho del vendedor = cantidadCompromisos × D, antes de retiros.

Después, los retiros acumulados más derechos pendientes deberán conservar ese

mismo total, excluyendo ETH ajeno al flujo del protocolo.

7.  Mantener modularidad, validaciones claras, eventos útiles y documentación de

funciones. La finalización, los retiros y la selección del ganador no podrán depender

de bucles sobre todos los participantes.

8.  Entregar un README con instrucciones reproducibles, decisiones de diseño,

supuestos y amenazas: secreto débil o perdido, reutilización de compromisos,

dependencia de timestamps, bloqueo por receptores y reentradas. Explicar que una

wallet no equivale a una persona y que el mecanismo no garantiza privacidad

permanente.

![](data:image/png;base64...)

![](data:image/png;base64...)