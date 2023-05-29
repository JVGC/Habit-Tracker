import { Header } from "./Header/Header";
import { SummaryTable } from "./SummaryTable/SummaryTable";
import { Container } from "./styles";

export function Home(){
    return(
        <Container>
            <Header />
            <SummaryTable />
        </Container>
    )
}