#  VN Sandbox Stress Test To-Do

1. **Event Volume Test**  
   - [✓] Auto-generate 1,000+ dummy events.  
   - [✓] Confirm sandbox loads all without huge slowdown/crash.  
   NB: initial load time is slightly larger, but no in game frame drops/buffering/loading.

2. **Trigger Collision Test**  
   - [ ] Create 100+ events with same trigger.  
   - [ ] Check all fire in order (priority/random as designed).  

3. **GameState Dependency Test**  
   - [ ] Add events with deep/nested gamestate conditions.  
   - [ ] Verify only correct ones fire.  

4. **Recursive/Chain Trigger Test**  
   - [ ] Build chained events A→B→C→…Z→A.  
   - [ ] Ensure sandbox avoids infinite loop (error/log/limit).  

5. **Concurrent Event Test**  
   - [ ] Set 100+ events to fire at same tick.  
   - [ ] Measure execution time, confirm no frame drop.  

6. **Corruption / Invalid Data Test**  
   - [ ] Add malformed metadata & duplicate labels.  
   - [ ] Sandbox should skip/log, not crash.  

7. **Endurance Test**  
   - [ ] Run auto simulation for 10,000 ticks (long session).  
   - [ ] Monitor memory/CPU; confirm no leaks.  

8. **Save/Load Integrity Test**  
   - [ ] Save mid-game with thousands of events active.  
   - [ ] Reload, confirm state + events fully intact.  
