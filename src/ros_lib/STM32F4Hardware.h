#ifndef _STM32F4_HARDWARE_H_
#define _STM32F4_HARDWARE_H_

extern "C"
{
    #include "main.h"
}

UART_HandleTypeDef UARTHandle;
uint8_t Buffer_1;
uint8_t *RxBuffer = &Buffer_1;

class STM32F4Hardware {
    public:
    STM32F4Hardware() {}
    void init() {
        UARTHandle.Instance = USART2;

        UARTHandle.Init.BaudRate = 57600;
        UARTHandle.Init.WordLength = UART_WORDLENGTH_8B;
        UARTHandle.Init.StopBits = UART_STOPBITS_1;
        UARTHandle.Init.Parity = UART_PARITY_NONE;
        UARTHandle.Init.HwFlowCtl = UART_HWCONTROL_NONE;
        UARTHandle.Init.Mode = UART_MODE_TX_RX;
        UARTHandle.Init.OverSampling = UART_OVERSAMPLING_16; // compensate baud error

        if(HAL_UART_DeInit(&UARTHandle) != HAL_OK) {
            Error_Handler();
        }
        if(HAL_UART_Init(&UARTHandle) != HAL_OK) {
            Error_Handler();
        }
    }

    int read() {
        if (HAL_UART_Receive(&UARTHandle, RxBuffer, 1 ,15) == HAL_OK) {
            return *RxBuffer;
        } else {
            return -1;
        }
    }

    void write(uint8_t *data, int length) {
        HAL_UART_Transmit(&UARTHandle, data, length, HAL_MAX_DELAY);
    }

    unsigned long time(void) {
        return HAL_GetTick();
    }
};

#endif
