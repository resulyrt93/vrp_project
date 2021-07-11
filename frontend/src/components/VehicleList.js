import React from 'react';
import {Button, Form, InputNumber, Space} from "antd";
import {MinusCircleOutlined, PlusOutlined} from "@ant-design/icons";

const VehicleList = ({onValuesChange}) => {
  return (
    <div>
      <Form onValuesChange={onValuesChange} autoComplete="off">
        <Form.List name="vehicles">
          {(fields, {add, remove}) => (
            <>
              {fields.map(({key, name, fieldKey, ...restField}) => (
                <Space key={key} style={{display: 'flex', marginBottom: 8}} align="baseline">
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
                    name={[name, 'location']}
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
      </Form>
    </div>
  );
};

export default VehicleList;