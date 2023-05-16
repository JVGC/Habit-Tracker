import React from 'react'
import ReactDOM from 'react-dom/client'
import { App } from './App.tsx'
import {ThemeProvider} from 'styled-components'

const theme = {
  background: '#09090A'
}

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <App />
    </ThemeProvider>
  </React.StrictMode>,
)
