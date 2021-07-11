import './App.css';
import 'antd/dist/antd.css';
import {Button, Card, Col, Drawer, Layout, Row, Space} from "antd";
import {Content} from "antd/es/layout/layout";
import React, {useState} from "react";
import VehicleList from "./components/VehicleList";
import JobList from "./components/JobList";
import {PlayCircleOutlined, SettingOutlined} from "@ant-design/icons";

function App() {

  const [data, setData] = useState({})
  const [visible, setVisible] = useState(false)

  const onJobListChanged = (value, values) => {
    setData({...data, jobs: values})
  }

  const onVehicleListChanged = (value, values) => {
    setData({...data, vehicles: values})
  }

  const solveRoute = () => {
    console.log("Solved")
  }

  const resultCardExtra = (
    <Space>
      <Button icon={<PlayCircleOutlined />} onClick={solveRoute}>Solve</Button>
      <Button icon={<SettingOutlined />} onClick={() => {setVisible(true)}}>Settings</Button>
    </Space>
  )

  return (
    <div className="App">
      <Layout style={{height: "100vh"}}>
        <Content style={{margin: '24px 16px 0'}}>
          <Row className="base-row" gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
            <Col className="base-column" span={6}>
              <Card title={"Vehicles"} className="card-template">
                <VehicleList onValuesChange={onVehicleListChanged}/>
              </Card>
            </Col>
            <Col className="base-column" span={6}>
              <Card title={"Jobs"} className="card-template">
                <JobList onValuesChange={onJobListChanged}/>
              </Card>
            </Col>
            <Col className="base-column" span={12}>
              <Card title={"Result"}
                    className="card-template"
                    extra={resultCardExtra}>
                Result
              </Card>
            </Col>
          </Row>
        </Content>
      </Layout>
      <Drawer
        title="Basic Drawer"
        placement="right"
        width={600}
        onClose={() => {setVisible(false)}}
        visible={visible}
      >
        <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p>
      </Drawer>
    </div>
  );
}

export default App;
