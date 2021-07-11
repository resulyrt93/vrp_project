import React from 'react';
import {Button, Col, Form, InputNumber, Row, Space} from "antd";
import {MinusCircleOutlined, PlusOutlined} from "@ant-design/icons";

const VehicleList = () => {

  return (
    <div>
      <Row style={{marginBottom: 10}}>
        <Col span={11}>Capacity</Col>
        <Col span={11}>Location Index</Col>
        <Col span={2}></Col>
      </Row>
      <Form.List name="vehicles">
        {(fields, {add, remove}) => (
          <>
            {fields.map(({key, name, fieldKey, ...restField}) => (
              <Space key={key} align="baseline">
                <Form.Item
                  {...restField}
                  name={[name, 'capacity']}
                  fieldKey={[fieldKey, 'capacity']}
                  rules={[{required: true, message: 'Missing capacity'}]}
                >
                  <InputNumber placeholder="Capacity"/>
                </Form.Item>
                <Form.Item
                  {...restField}
                  name={[name, 'start_index']}
                  fieldKey={[fieldKey, 'location']}
                  rules={[{required: true, message: 'Missing Location Index'}]}
                >
                  <InputNumber placeholder="Location Index"/>
                </Form.Item>
                <MinusCircleOutlined onClick={() => remove(name)}/>
              </Space>
            ))}
            <Form.Item>
              <Button type="dashed" onClick={() => add()} block icon={<PlusOutlined/>}>
                Add Vehicle
              </Button>
            </Form.Item>
          </>
        )}
      </Form.List>
    </div>
  );
};

export default VehicleList;