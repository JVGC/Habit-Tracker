import { Container, GlobalStyle, Home } from "./styles/global"
import { Header } from "./components/Header/Header"
import { SummaryTable } from "./components/SummaryTable/SummaryTable"

import './styles/global.css'

export function App() {

  return (
  <>
    <GlobalStyle />
    <Container>
      <Home>
        <Header />
        <SummaryTable />
      </Home>
    </Container>
  </>
  )
}