import { render, screen } from "@testing-library/react";

function TestComponent() {
    return <h1>AstraAtlas</h1>
}

test("renders title", () => {
    render(<TestComponent />);
    expect(screen.getByText("AstraAtlas")).toBeInTheDocument();
})