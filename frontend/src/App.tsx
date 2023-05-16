import { Container, GlobalStyle, Home } from "./styles/global"
import { Header } from "./components/Header/Header"
import { SummaryTable } from "./components/SummaryTable/SummaryTable"


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