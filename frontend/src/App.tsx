import { Container, Home } from "./styles/global"
import { Header } from "./components/Header/Header"
import { SummaryTable } from "./components/SummaryTable/SummaryTable"

export function App() {

  return (
    <Container>
      <Home>
        <Header />
        <SummaryTable />
      </Home>
    </Container>
  )
}