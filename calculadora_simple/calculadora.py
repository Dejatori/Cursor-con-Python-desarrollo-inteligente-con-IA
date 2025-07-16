#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Simple - Aplicación de consola para operaciones aritméticas básicas

Este script implementa una calculadora simple que permite realizar operaciones
de suma, resta, multiplicación y división. El programa continúa ejecutándose
hasta que el usuario ingrese "salir" como operación.

Autor: Dejatori
Versión: 1.0
"""

def obtener_numero(mensaje):
    """
    Solicita al usuario un número y valida que sea numérico.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        float: Número ingresado por el usuario
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Por favor ingresa un número válido.")

def realizar_operacion(operacion, num1, num2):
    """
    Realiza la operación aritmética especificada entre dos números.
    
    Args:
        operacion (str): Tipo de operación a realizar
        num1 (float): Primer número
        num2 (float): Segundo número
        
    Returns:
        float: Resultado de la operación
    """
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 == 0:
            raise ValueError("No se puede dividir por cero")
        return num1 / num2
    else:
        raise ValueError(f"Operación '{operacion}' no válida")

def mostrar_menu():
    """
    Muestra el menú de operaciones disponibles.
    """
    print("\n" + "="*50)
    print("🧮 CALCULADORA SIMPLE")
    print("="*50)
    print("Operaciones disponibles:")
    print("  • suma")
    print("  • resta") 
    print("  • multiplicacion")
    print("  • division")
    print("  • salir (para terminar)")
    print("="*50)

def main():
    """
    Función principal que ejecuta el bucle de la calculadora.
    """
    print("¡Bienvenido a la Calculadora Simple! 🎉")
    
    while True:
        # Mostrar menú de operaciones
        mostrar_menu()
        
        # Solicitar operación al usuario
        operacion = input("\n📝 Ingresa la operación que deseas realizar: ").lower().strip()
        
        # Verificar si el usuario quiere salir
        if operacion == "salir":
            print("\n👋 ¡Gracias por usar la Calculadora Simple! ¡Hasta luego!")
            break
        
        # Validar que la operación sea válida
        operaciones_validas = ["suma", "resta", "multiplicacion", "division"]
        if operacion not in operaciones_validas:
            print(f"❌ Error: '{operacion}' no es una operación válida.")
            print("Operaciones válidas:", ", ".join(operaciones_validas))
            continue
        
        # Solicitar los dos números
        print(f"\n🔢 Ingresa los números para la operación: {operacion}")
        num1 = obtener_numero("Primer número: ")
        num2 = obtener_numero("Segundo número: ")
        
        # Realizar la operación y mostrar el resultado
        try:
            resultado = realizar_operacion(operacion, num1, num2)
            
            # Mostrar el resultado de forma clara
            print("\n" + "-"*30)
            print("📊 RESULTADO:")
            print(f"{num1} {operacion} {num2} = {resultado}")
            print("-"*30)
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    # Manejar interrupción del teclado (Ctrl+C) de forma elegante
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario. ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error crítico: {e}")
        print("El programa se cerrará.")
