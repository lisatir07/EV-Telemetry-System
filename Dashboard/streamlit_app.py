import streamlit as st
import pandas as pd
import telemetry
import time
import data_logger

st.title("EV Telemetry Dashboard")

# contains a spot for updated values
placeholder = st.empty()

#updates values 
while True:
    
    #retrieve data
    data = telemetry.get_telemetry()

    #save data
    data_logger.save_data(data)

    with placeholder.container():

        #display numeric data in a row

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Battery Voltage",
                f"{data['battery_voltage']} V"
            )

        with col2:
            st.metric(
                "Motor Temperature",
                f"{data['motor_temperature']} °C"
            )
       
        with col3:
            st.metric(
                "Throttle",
                f"{data['throttle']} %"
            )

            st.progress(data["throttle"] / 100)

        with col4:

        #change colour based on system status using HTML
            if data["system_status"] == "OK":
                color = "green"
            else:
                color = "red"

            st.markdown(
                f"""
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 10px;
                ">
                    <div style="
                        width: 20px;
                        height: 20px;
                        background-color: {color};
                        border-radius: 50%;
                    "></div>

                    Status:
                    {data['system_status']}
                </div>
                """,
                unsafe_allow_html=True

            )

        #plot battery voltage
        
        st.subheader("Battery Voltage")
        df = pd.read_csv("telemetry_data.csv")
        st.line_chart(
            df["battery_voltage"]
        )

        #plot motor temperature
        st.subheader("Motor Temperature")
        st.line_chart(
            df['motor_temperature']
        )

        #plot throttle
        st.subheader("Throttle")
        st.line_chart(
            df['throttle']
        )

    time.sleep(1)