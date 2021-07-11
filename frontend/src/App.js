import './App.css';
import 'antd/dist/antd.css';
import {Button, Card, Col, Drawer, Form, Layout, Row, Space, message, Spin} from "antd";
import {Content} from "antd/es/layout/layout";
import React, {useState} from "react";
import VehicleList from "./components/VehicleList";
import JobList from "./components/JobList";
import {PlayCircleOutlined, SettingOutlined} from "@ant-design/icons";
import DrawerContent from "./components/DrawerContent";
import {dummyData} from "./dummy.json"
import useSolver from "./hooks/useSolver"
import ResultList from "./components/ResultList";

function App() {

  const [form] = Form.useForm()
  const [visible, setVisible] = useState(false)
  const [resultData, setResultData] = useState([])
  const [loading, setLoading] = useState(false)
  const {solve} = useSolver()

  const solveRoute = async () => {
    setLoading(true)
    setResultData([])
    const data = form.getFieldsValue()
    try {
      const result = await solve(data)
      setResultData(result)
    } catch (e) {
      message.warn("Error : ", e)
    } finally {
      setLoading(false)
    }
  }

  const resultCardExtra = (
    <Space>
      <Button icon={<PlayCircleOutlined/>} onClick={solveRoute}>Solve</Button>
      <Button icon={<SettingOutlined/>} onClick={() => {
        setVisible(true)
      }}>Settings</Button>
    </Space>
  )

  const initialValues = {...dummyData, matrix: JSON.stringify(dummyData.matrix, null, 2)}

  return (
    <div className="App">
      <Form
        initialValues={initialValues}
        form={form}>
        <Spin tip={"Please Wait..."} spinning={loading}>
          <Layout style={{height: "100vh"}}>
            <Content style={{margin: '24px 16px 0'}}>
              <Row className="base-row" gutter={{xs: 8, sm: 16, md: 24, lg: 32}}>
                <Col className="base-column" span={6}>
                  <Card title={"Vehicles"} className="card-template">
                    <VehicleList/>
                  </Card>
                </Col>
                <Col className="base-column" span={8}>
                  <Card title={"Jobs"} className="card-template">
                    <JobList/>
                  </Card>
                </Col>
                <Col className="base-column" span={10}>
                  <Card title={"Result"}
                        className="card-template"
                        extra={resultCardExtra}>
                    <ResultList resultData={resultData}/>
                  </Card>
                </Col>
              </Row>
            </Content>
          </Layout>
        </Spin>
        <Drawer
          title="Settings"
          placement="right"
          width={600}
          onClose={() => {
            setVisible(false)
          }}
          visible={visible}
        >
          <DrawerContent/>
        </Drawer>
      </Form>
    </div>
  );
}

export default App;
