

class Cheap_Thrills_App extends React.Component {
    render () {
        const title = "Cheap Thrills"
        const subtitle = "Free Events in the Bay Area"
        return (
            <div>
                <Header title={title} subtitle={subtitle} />
            </div>
        );

    }

}

class Header extends React.Component {
  render(){
    return (
      <div>
        <h1>{this.props.title}</h1>
        <h2>{this.props.subtitle}</h2>
      </div>
    );
  }

}