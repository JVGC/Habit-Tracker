import { Home } from "./pages/Home/Home"
import { Container, GlobalStyle } from "./styles/global"

export function App() {

  return (
  <>
    <GlobalStyle />
    <Container>
      <Home />
    </Container>
  </>
  )
}