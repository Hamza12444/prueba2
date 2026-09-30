## 1. Fase de Análisis

* **Descripción del problema:** Desarrollar un programa que calcule el descuento aplicable a una compra basándose en su importe total.
* **Entradas:** 
  * `importe` (tipo `float`): Cantidad total de la compra en euros introducida por el usuario.
* **Salidas:** 
  * Porcentaje de descuento aplicado (0%, 10% o 15%).
  * Cantidad descontada en euros.
  * Precio final a pagar.
* **Restricciones:** 
  * El importe debe ser un número real mayor o igual a 0.
  * Control de errores ante entradas no numéricas o valores negativos.

---

## 2. Fase de Diseño

### Pseudocódigo
```text
INICIO
    ESCRIBIR "Introduce el importe de la compra (€):"
    LEER importe
    
    SI importe < 0 ENTONCES
        ESCRIBIR "Error: El importe no puede ser negativo."
    SINO
        SI importe >= 300 ENTONCES
            porcentaje <- 15
        SINO SI importe >= 100 ENTONCES
            porcentaje <- 10
        SINO
            porcentaje <- 0
        FIN SI
        
        descuento <- importe * (porcentaje / 100)
        total_pagar <- importe - descuento
        
        ESCRIBIR "Descuento aplicado:", porcentaje, "%"
        ESCRIBIR "Cantidad descontada:", descuento, "€"
        ESCRIBIR "Total a pagar:", total_pagar, "€"
    FIN SI
FIN